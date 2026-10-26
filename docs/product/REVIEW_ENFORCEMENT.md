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
| `web/src/lib/data/demo/identities.json` | author identities (import contract v2), once it lands |
| `.github/CODEOWNERS` | the list itself |

## The blocking limitation: one GitHub identity

[Certain] Every pull request on this repository is opened and merged as **`bemrick2`**: #276, #280 and #283 all show `author=bemrick2` and `merged_by=bemrick2`. That includes the ones Claude sessions open. `bemrick2` is the owner, the only code owner and the repository admin.

GitHub never lets a pull request's author approve it. So with today's setup, **owner review can't be enforced in a meaningful way**:
- If code-owner review is required, a session's PR that touches `reviewers.json` can never get the owner's approval, because the owner *is* the author. It could merge only through an admin bypass, and the admin is the same account the sessions use.
- If admin bypass is allowed, anything with that token can merge without review.

**Prerequisite (owner action):** give automated sessions their own GitHub identity, not `bemrick2`. Then `bemrick2` reviews as the owner, and the sessions can't approve or bypass. The options:
1. A **machine user** (a second GitHub account) added as a collaborator with **Write**, not Admin. Sessions' git and `gh` tokens belong to it.
2. A **GitHub App** installed on the repository with *contents: write* and *pull requests: write*. It is not an admin and isn't on any bypass list.

Whichever is chosen, `bemrick2` stays the only admin and the only code owner, and no session token can belong to `bemrick2`.

## Availability on this account

- [Certain] The repository is **public** and owned by a **user**, not an organization.
- [Likely] For public repositories, GitHub provides branch protection, repository rulesets, required pull-request reviews, required code-owner review and required status checks on every plan, Free included.
- [Guessing] This session can't read the account's plan (`GET /user` returns `plan: null`, and `/users/*` is blocked here). If the repository is ever made **private**, these features need **GitHub Pro** on a personal account.
- **Not available for user-owned repositories:** push rulesets that restrict changes by file path. Those need an organization. So a rule can't say "only these files need review". The rule below applies to every PR into `main`, and code-owner review adds the owner's approval only for the files above.

## Exact settings: one repository ruleset on `main`

Create it under **Settings → Rules → Rulesets → New branch ruleset**, or as the owner with `POST /repos/bemrick2/CollegePrep/rulesets` and the body below. Set it up **only after** the prerequisite above. Otherwise every session PR into `main` stops at review.

```json
{
  "name": "main: reviewed, checked, owner-approved editorial records",
  "target": "branch",
  "enforcement": "active",
  "conditions": { "ref_name": { "include": ["~DEFAULT_BRANCH"], "exclude": [] } },
  "bypass_actors": [],
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
          { "context": "validate" }, { "context": "database" },
          { "context": "mutation (1)" }, { "context": "mutation (2)" }, { "context": "mutation (3)" }, { "context": "mutation (4)" },
          { "context": "mutation (5)" }, { "context": "mutation (6)" }, { "context": "mutation (7)" }, { "context": "mutation (8)" }
        ]
    } }
  ]
}
```

What each setting does:
- **`bypass_actors: []`.** Nobody bypasses, admins included. The owner merges through the same rules as everyone else.
- **`require_code_owner_review`.** A PR touching any file in `CODEOWNERS` needs `bemrick2`'s approval.
- **`dismiss_stale_reviews_on_push` and `require_last_push_approval`.** A change pushed after approval needs a new approval, from someone other than the person who pushed it.
- **`required_approving_review_count: 1`.** This applies to **every** PR into `main`, not only editorial ones, because user-owned repositories can't scope reviews by path. That means Research's and Deep Dive's data PRs need one approval too.
  - If that's too much, set it to `0` and keep `require_code_owner_review: true`. [Guessing] GitHub then still requires the code owner on owned files. **Test this before relying on it:** open one PR that touches only a doc and one that touches `reviewers.json`, and check that only the second asks for `bemrick2`.
- **Required checks.** These are the jobs that run on *every* PR into `main` (`validate-data.yml` has no path filter). `web` and `local-backend` (`web.yml`) are left out on purpose: they have path filters, so a required `web` check would leave PRs that don't touch `web/**` waiting forever.
  - To require them as well, first remove the `paths:` filter from `web.yml`'s `pull_request` trigger.
- **`non_fast_forward` and `deletion`.** No force pushes or deletion of `main`.

## Classic branch protection, if rulesets aren't used

Under **Settings → Branches → Add rule for `main`**:
- Require a pull request before merging, with 1 approval.
- Dismiss stale approvals.
- Require review from Code Owners.
- Require approval of the most recent push.
- Require status checks: the same ten contexts.
- **Do not allow bypassing the above settings**, which in the API is `enforce_admins: true`.
- Restrict force pushes and deletions.

## What stays outside GitHub's protection

- **Reviewer identity** is the registry's job, not GitHub's. A reviewer id on a sheet is still only what the sheet says (`QUESTION_REVIEW_WORKFLOW.md`).
- **The workflows' bot pushes** (`ipeds-source`, `program-research`, `research-pipeline`) go to their own branches, never `main`, so a ruleset on `main` doesn't affect them.
- **Hosted data** (Supabase) isn't covered by repository rules. Publication there has its own server gates (CR-21, CR-24, CR-23) and stays held.

## How to check it's working (owner, after setup)

1. From the session identity, open a PR that changes only `reviewers.json`. **Pass:** it can't merge until `bemrick2` approves, and the session identity can neither approve it nor merge it.
2. Push one more commit to that PR. **Pass:** the earlier approval is dismissed.
3. Open a PR that changes only a doc. **Pass:** the code owner isn't required (with count 0), or one approval is (with count 1).
4. Try to merge with `mutation (3)` failing. **Pass:** the merge is blocked.
