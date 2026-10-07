#!/usr/bin/env python3
"""Durable retention of the fetched documents behind every promoted record.

Run branches (`pipeline-run/**`, `program-run/**`) hold the fetched pages, CourseLeaf layout documents and PDF layouts,
and are never merged; local `pipeline/runs/` and `programs/runs/` copies are git-ignored. A promoted record's evidence
(`sources/<pipeline|programs>/<STATE>/<run>/evidence.json`) names each document by page file and sha256, so the
documents themselves must stay reachable for verification to be reproduced.

  python scripts/retain_evidence.py            locate each archive's run, write retention.json beside evidence.json, and add
                                               every retained document to the content-addressed `evidence-store` branch
                                               (documents/<blob[:2]>/<blob>.json.gz: the exact bytes, keyed by git blob id)
  python scripts/retain_evidence.py --push     ... and push evidence-store
  python scripts/retain_evidence.py --verify-store   every retained document is in origin/evidence-store with its blob id
  python scripts/retain_evidence.py --check    offline: every evidence archive has a retention.json that lists every
                                               cited document and, for layout-read rows, the layout document

retention.json lists every retained document with its role, URL, sha256 and git blob id; `evidence-store` keeps the bytes
(append-only, one branch for every run), so verification can be reproduced after a run branch is deleted.
"""
from __future__ import annotations
import json, subprocess, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'pipeline': 'pipeline/runs', 'programs': 'programs/runs'}
STORE = 'evidence-store'
LAYOUT_ROLES = {'courselist', 'outline', 'pdf_layout'}
LAYOUT_EXTRACTORS = {'courselist_html/v1'}


def git(*a, binary=False):
    r = subprocess.run(['git', *a], cwd=ROOT, capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode()


def archives():
    for kind in KINDS:
        for ev in sorted((ROOT / 'sources' / kind).glob('*/*/evidence.json')):
            yield kind, ev.parent.parent.name, ev.parent.name, ev


def cited(ev_path):
    """(page files, urls, layout-read urls) cited by an evidence archive."""
    pages, urls, layout_urls = set(), set(), set()
    for v in json.loads(ev_path.read_text()).values():
        src = v.get('source') if isinstance(v, dict) else None
        if not src: continue
        if src.get('page_file'): pages.add(src['page_file'])
        u = src.get('requested_url') or src.get('url')
        if u: urls.add(u)
        if v.get('extractor') in LAYOUT_EXTRACTORS and u: layout_urls.add(u)
        ls = v.get('layout_source')
        if ls and ls.get('url'): layout_urls.add(ls['url'].split('#')[0])
    return pages, urls, layout_urls


def run_index():
    """run dir -> [(branch, commit)] across every remote run branch."""
    idx = defaultdict(list)
    heads = [l.split() for l in git('for-each-ref', '--format=%(refname:short) %(objectname)', 'refs/remotes/origin').splitlines()]
    for ref, sha in heads:
        if '/' not in ref: continue
        b = ref.split('/', 1)[1]
        if not b.startswith(('pipeline-run/', 'program-run/')): continue
        for base in KINDS.values():
            try: names = git('ls-tree', '-d', '--name-only', f'{sha}:{base}').split()
            except subprocess.CalledProcessError: continue
            for st in names:
                for run in git('ls-tree', '-d', '--name-only', f'{sha}:{base}/{st}').split():
                    idx[f'{base}/{st}/{run}'].append((b, sha))
    return idx


def manifest(sha, run_dir):
    out = []
    for line in git('show', f'{sha}:{run_dir}/manifest.jsonl').splitlines():
        try: out.append(json.loads(line))
        except ValueError: pass
    return out


def blobs(sha, run_dir):
    out = {}
    for line in git('ls-tree', '-r', f'{sha}:{run_dir}/pages').splitlines():
        meta, name = line.split('\t'); out[name] = meta.split()[2]
    return out


def retain(push=False):
    idx = run_index(); tags = []
    for kind, st, run, ev in archives():
        run_dir = f'{KINDS[kind]}/{st}/{run}'
        pages, urls, layout_urls = cited(ev)
        best = None
        for b, sha in idx.get(run_dir, []):
            bl = blobs(sha, run_dir)
            have = len(pages & set(bl))
            if best is None or have > best[3]: best = (b, sha, bl, have)
        out = {'kind': kind, 'run_dir': run_dir, 'evidence': str(ev.relative_to(ROOT))}
        if not best:
            out.update(run_branch=None, documents=[], missing=sorted(pages), note='no run branch holds this run directory')
        else:
            b, sha, bl, _ = best
            m = manifest(sha, run_dir)
            docs = {}
            for e in m:
                pf = e.get('page_file')
                if not pf: continue
                url = e.get('url') or ''
                if pf in pages or (e.get('role') in LAYOUT_ROLES and (e.get('via') in urls or url.split('#')[0] in layout_urls)):
                    if pf in bl: docs[(pf, url)] = {'page_file': pf, 'blob': bl[pf], 'role': e.get('role'), 'url': url, 'sha256': e.get('sha256')}
            layouts = {d['url'].split('#')[0] for d in docs.values() if d['role'] in LAYOUT_ROLES}
            for d in docs.values(): d['store_path'] = store_path(d)
            tags.append(docs.values())
            out.update(run_branch=b, commit=sha, store=STORE, documents=sorted(docs.values(), key=lambda d: (d['page_file'], d['url'])),
                       missing=sorted(pages - {k[0] for k in docs}),
                       layout_missing=sorted(u for u in layout_urls if u not in layouts))
        (ev.parent / 'retention.json').write_text(json.dumps(out, indent=1, sort_keys=True) + '\n')
        print(f"{run_dir}: {len(out['documents'])} documents, missing {len(out['missing'])}, layout missing {len(out.get('layout_missing', []))}"
              + ('' if out.get('run_branch') else ' (NO RUN BRANCH)'))
    commit = update_store([d for ds in tags for d in ds])
    if push: git('push', '-q', 'origin', f'{commit}:refs/heads/{STORE}')
    return 0


def store_path(d):
    return f"documents/{d['blob'][:2]}/{d['blob']}.json.gz"


def mktree(entries):
    return git_in('mktree', ''.join(f'{mode} {kind} {sha}\t{name}\n' for mode, kind, sha, name in sorted(entries, key=lambda e: e[3]))).strip()


def git_in(*a):
    """git with the last argument as standard input."""
    return subprocess.run(['git', *a[:-1]], cwd=ROOT, input=a[-1], capture_output=True, text=True, check=True).stdout


def update_store(docs):
    """Append documents to evidence-store (content-addressed by git blob id; existing entries are kept)."""
    have = {}
    try:
        parent = git('rev-parse', f'refs/remotes/origin/{STORE}').strip()
        for line in git('ls-tree', '-r', parent).splitlines():
            meta, path = line.split('\t'); have[path] = meta.split()[2]
    except subprocess.CalledProcessError: parent = None
    for d in docs:
        p = d['store_path']
        if p in have and have[p] != d['blob']: raise SystemExit(f'{p}: store holds different bytes than {d["blob"]}')
        have[p] = d['blob']
    by_prefix = defaultdict(list)
    for path, blob in have.items():
        _, prefix, name = path.split('/'); by_prefix[prefix].append(('100644', 'blob', blob, name))
    docs_tree = mktree([('040000', 'tree', mktree(v), k) for k, v in by_prefix.items()])
    readme = git_in('hash-object', '-w', '--stdin', 'Retained evidence documents for CollegePrep (scripts/retain_evidence.py). Append-only: '
                    'documents/<blob[:2]>/<blob>.json.gz (git blob ids of the exact bytes) are the fetched pages and layout documents cited by sources/*/*/*/evidence.json.\n').strip()
    root = mktree([('040000', 'tree', docs_tree, 'documents'), ('100644', 'blob', readme, 'README.md')])
    if parent and git('rev-parse', f'{parent}^{{tree}}').strip() == root: return parent
    args = ['commit-tree', root] + (['-p', parent] if parent else []) + ['-m', f'Retain {len(have)} evidence documents']
    commit = git(*args).strip()
    print(f'{STORE}: {len(have)} documents, commit {commit[:12]}')
    return commit


def verify_store():
    try: tree = git('ls-tree', '-r', f'refs/remotes/origin/{STORE}')
    except subprocess.CalledProcessError: print(f'origin/{STORE} not fetched'); return 1
    have = {l.split('\t')[1]: l.split()[2] for l in tree.splitlines()}
    bad = [f"{d['store_path']} ({r})" for r in sorted((ROOT / 'sources').glob('*/*/*/retention.json'))
           for d in json.loads(r.read_text()).get('documents', []) if have.get(d.get('store_path')) != d['blob']]
    if bad: print(f'{len(bad)} retained documents missing from {STORE}, e.g. {bad[0]}'); return 1
    print(f'{STORE} holds every retained document'); return 0


def check():
    bad = []
    for kind, st, run, ev in archives():
        rp = ev.parent / 'retention.json'
        if not rp.exists(): bad.append(f'{ev.parent}: no retention.json (run python scripts/retain_evidence.py)'); continue
        r = json.loads(rp.read_text())
        pages, urls, layout_urls = cited(ev)
        listed = {d['page_file'] for d in r.get('documents', [])}
        if not r.get('store') or any(not d.get('store_path') for d in r.get('documents', [])): bad.append(f'{ev.parent}: documents not in the evidence store')
        lost = sorted(pages - listed)
        if lost: bad.append(f'{ev.parent}: {len(lost)} cited documents not retained, e.g. {lost[0]}')
        layouts = {d['url'].split('#')[0] for d in r.get('documents', []) if d.get('role') in LAYOUT_ROLES}
        nolayout = sorted(u for u in layout_urls if u not in layouts)
        if nolayout: bad.append(f'{ev.parent}: {len(nolayout)} layout-read pages without a retained layout document, e.g. {nolayout[0]}')
    if bad: print('\n'.join(bad)); return 1
    print('Evidence retention complete for every archive'); return 0


if __name__ == '__main__':
    raise SystemExit(check() if '--check' in sys.argv else verify_store() if '--verify-store' in sys.argv else retain(push='--push' in sys.argv))
