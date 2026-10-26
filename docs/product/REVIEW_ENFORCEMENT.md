# Enforcing owner review of reviewer appointments and editorial approvals

**Status (checked 2026-10-26 through the GitHub API):** not enforced.
- `main` has no branch protection and no rulesets: `GET …/branches/main` reports `protected: false`, and `GET …/rulesets` returns `[]`.
- `.github/CODEOWNERS` lists the review records, but on its own it only *requests* the owner's review. GitHub enforces it only when a ruleset or branch protection requires code-owner review. **CODEOWNERS alone is not protection.**

## What we're protecting

Changes to these files decide who may review and what counts as approved:

| File | Holds |
|---|---|
| `web/src/lib/data/demo/reviewers.json` | reviewer appointments (`reviewerRegistry.ts`) |
| `web/src/lib/data/demo/editorialLedger.json` | sign-offs and approvals |
| `web/src/lib/data/demo/identities.json` | author identities (import contract v2, #290) |
| `.github/CODEOWNERS` | the list itself |
| `.github/workflows/` | the required checks; a PR that edits a workflow could otherwise weaken a check it must pass |

This PR adds the last three to `.github/CODEOWNERS`; before it, only `reviewers.json` and `editorialLedger.json` were listed.

## The blocking limitation: one GitHub identity

[Certain] Every pull request on this repository is opened and merged as **`bemrick2`**: #276, #280 and #283 all show `author=bemrick2` and `merged_by=bemrick2`. That includes the ones Claude sessions open. `bemrick2` is the owner, the only code owner and the repository admin.

GitHub never lets a pull request's author approve it. So with today's setup, **owner review can't be enforced in a meaningful way**:
- If code-owner review is required, a session's PR that touches `reviewers.json` can never get the owner's approval, because the owner *is* the author. It could merge only through an admin bypass, and the admin is the same account the sessions use.
- If admin bypass is allowed, anything with that token can merge without review.

**Prerequisite (owner action):** give automated sessions their own GitHub identity, not `bemrick2`. Then `bemrick2` reviews as the owner, and the sessions can't approve their own PRs or bypass. (A session identity with Write access can approve a PR that `bemrick2` opens, which satisfies the approval count; code-owned files still need `bemrick2`, the only code owner.) The options:
1. A **machine user** (a second GitHub account) added as a collaborator with **Write**, not Admin. Sessions' git and `gh` tokens belong to it.
2. A **GitHub App** installed on the repository with *contents: write* and *pull requests: write*. It is not an admin and isn't on any bypass list.

Whichever is chosen, `bemrick2` stays the only admin and the only code owner, and no session token can belong to `bemrick2`.

## Availability on this account

- [Certain] The repository is **public** and owned by a **user**, not an organization.
- [Certain] (GitHub's "About rulesets" and branch-protection docs) For public repositories, GitHub provides branch protection, repository rulesets, required pull-request reviews, required code-owner review and required status checks on every plan, Free included.
- [Certain] This session can't read the account's plan (`GET /user` returns `plan: null`, and `/users/*` is blocked here). The plan doesn't matter while the repository is public. If it is ever made **private**, these features need **GitHub Pro** (or higher) on a personal account (GitHub docs).
- **Not available here: path-scoped review requirements.** [Certain] A ruleset's pull-request rule can require specific reviewers for specific paths (`required_reviewers`) only with teams, and teams exist only in organizations (the REST schema allows only `Team` reviewers). So a rule can't say "only these files need an approval". Code-owner review is the path-scoped part that does work: it adds the owner's approval only for files in `CODEOWNERS`. (Push rulesets, which restrict who may push changes to given paths, are a separate feature, offered for private and internal repositories on the Team plan; they wouldn't help here either.)

## Exact settings: one repository ruleset on `main`

Create it under **Settings → Rules → Rulesets → New branch ruleset**, or as the owner with `POST /repos/bemrick2/CollegePrep/rulesets` and the body below. Set it up **only after** the prerequisite above. Otherwise every session PR into `main` stops at review.

```json
{
  "name": "main: reviewed, checked, owner-approved editorial records",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "bypass_actors": [
    { "actor_type": "RepositoryRole", "actor_id": 5, "bypass_mode": "pull_request" }
  ],
  "rules": [
    { "type": "deletion" },
    { "type": "non_fast_forward" },
    { "type": "pull_request", "parameters": {
        "required_approving_review_count": 1,
        "require_code_owner_review": true,
        "dismiss_stale_reviews_on_push": true,
        "require_last_push_approval": true,
        "required_review_thread_resolution": false
    } },
    { "type": "required_status_checks", "parameters": {
        "strict_required_status_checks_policy": false,
        "required_status_checks": [
          { "context": "validate", "integration_id": 15368 }, { "context": "database", "integration_id": 15368 },
          { "context": "mutation (1)", "integration_id": 15368 }, { "context": "mutation (2)", "integration_id": 15368 },
          { "context": "mutation (3)", "integration_id": 15368 }, { "context": "mutation (4)", "integration_id": 15368 },
          { "context": "mutation (5)", "integration_id": 15368 }, { "context": "mutation (6)", "integration_id": 15368 },
          { "context": "mutation (7)", "integration_id": 15368 }, { "context": "mutation (8)", "integration_id": 15368 }
        ]
    } }
  ]
}
```

What each setting does:
- **The owner's own PRs would deadlock without a bypass.** GitHub never lets a PR's author approve it, and `bemrick2` is the only code owner. So a PR that `bemrick2` opens (or last pushes to) and that touches a code-owned file can never get a code-owner approval.
  - **`bypass_actors`** therefore lists the repository **admin** role in `pull_request` mode. An admin may merge such a PR through the pull-request page, but can't push straight to `main`.
  - [Likely] `actor_id: 5` is the admin repository role; confirm it in the ruleset form (Bypass list → Add bypass → Repository admin) or from the ruleset GET after creating it.
  - This is safe only because of the prerequisite: `bemrick2` stays the only admin, and no session token is an admin. A session can't bypass; the owner can, and every bypass shows in the ruleset's insights. The bypass covers **every** rule in the ruleset, failing required checks included, so the owner merging past a red check is possible and is the owner's call.
- **`require_code_owner_review`.** A PR touching any file in `CODEOWNERS` needs `bemrick2`'s approval.
- **`dismiss_stale_reviews_on_push` and `require_last_push_approval`.** A change pushed after approval needs a new approval, from someone other than the person who pushed it. If the owner pushes the last commit to a session's PR, only the owner's bypass can merge it.
- **`required_approving_review_count: 1`.** This applies to **every** PR into `main`, not only editorial ones (see "path-scoped review requirements" above). With `bemrick2` as the only other person, **count 1 means the owner approves every PR**, including Research's and Deep Dive's data PRs.
  - **Recommended: keep count 1.** The alternative, `0` with `require_code_owner_review: true`, would require the code owner only on code-owned files ([Likely]). It is **not safe here**: the code that interprets the records (`reviewerRegistry.ts`, `editorialLedger.ts`, `authorIdentity.ts`, `questionCandidates.ts`, `editorialReview.ts`) and the scripts the required checks run (`scripts/validate_data.py`, `scripts/mutation_check.py`, `tests/`, `supabase/tests/`) aren't code-owned. With count 0 a PR could make the code ignore registry problems, or weaken a check, with no approval and without touching a data file. Count 0 would be reasonable only if all of those were added to `CODEOWNERS` too, which in practice is most of the repository.
  - **Test it before relying on it:** open one PR that touches only a doc and one that touches `reviewers.json`, and check that only the second asks for `bemrick2`.
- **Required checks.** These are the jobs that run on *every* PR into `main` (`validate-data.yml` has no path filter). `integration_id: 15368` is the GitHub Actions app (read from this PR's check runs), so only Actions can satisfy them, not a status posted by any other token with the same name.
  - `web` and `local-backend` (`web.yml`) are left out on purpose. They have path filters, so a required `web` check would leave PRs that don't touch `web/**` waiting forever.
  - To require them as well, either remove the `paths:` filter from `web.yml`'s `pull_request` trigger (then every PR waits for them, a few minutes each), or keep the trigger unfiltered and decide **inside** each job, at the step level, whether there's anything to run. Avoid a job-level `if:` fed by a separate "changes" job: a job skipped by `if:` reports success, and if the changes job itself fails, the dependent jobs are skipped and the required check passes without running anything.
- **`non_fast_forward` and `deletion`.** No force pushes or deletion of `main`.

## Classic branch protection, if rulesets aren't used

Under **Settings → Branches → Add rule for `main`**:
- Require a pull request before merging, with 1 approval.
- Dismiss stale approvals.
- Require review from Code Owners.
- Require approval of the most recent push.
- Require status checks: the same ten contexts, from the GitHub Actions app.
- **Bypass:** classic protection has no per-mode bypass. With `enforce_admins: true` ("Do not allow bypassing the above settings"), the owner's own PRs to code-owned files deadlock (see above). With it off, the admin can merge anything, including by direct push. That's why the ruleset is the recommended form.
- Restrict force pushes and deletions.

## What stays outside GitHub's protection

- **Reviewer identity** is the registry's job, not GitHub's. A reviewer id on a sheet is still only what the sheet says (`QUESTION_REVIEW_WORKFLOW.md`).
- **The workflows' bot pushes** (`ipeds-source`, `program-research`, `research-pipeline`) go to their own branches, never `main`, so a ruleset on `main` doesn't affect them.
- **Hosted data** (Supabase) isn't covered by repository rules. Publication there has its own server gates (CR-21, CR-24, CR-23) and stays held.

## How to check it's working (owner, after setup)

1. From the session identity, open a PR that changes only `reviewers.json`. **Pass:** it can't merge until `bemrick2` approves, and the session identity can neither approve it nor merge it.
2. Push one more commit to that PR. **Pass:** the earlier approval is dismissed.
3. Open a PR that changes only a doc. **Pass:** the code owner isn't required (with count 0), or one approval is (with count 1).
4. From the **session identity**, try to merge with `mutation (3)` failing. **Pass:** the merge is blocked. (The owner's bypass would let the owner merge it; that's expected.)
