# HireOps Progress

Last updated: 2026-09-03 (Week 1, Day 1)

## Done
### W1D1: Repository foundation
- [x] Repo cloned to Linux filesystem (~/projects/hireops)
- [x] Git identity + WSL-safe config (autocrlf=input, pull.rebase=true)
- [x] .gitattributes, .gitignore, .editorconfig
- [x] README.md skeleton
- [x] docs/adr/0001-branching-and-release-strategy.md
- [x] First commit; main + dev pushed
- [x] Branch ruleset `protect-main` (PR required, 0 approvals, linear, no force push, no deletion)
- [x] Tag ruleset `protect-release-tags` on v* (no updates, no deletions)
- [x] Loop proven: dev -> PR #1 -> main -> tag v0.0.1
- [x] Direct push to main verified as REJECTED

## In progress
- W1D2: FastAPI app skeleton (not started)

## Blocked
- (none)

## Decisions
- AWS region: us-east-2
- AWS account: root MFA enabled; IAM admin user NOT yet created (W3 D1)
- Budget alarms: hireops (80/100 actual, 100 forecasted), hireops-monthly-50 (100 actual)

## Deferred / dropped
- Domain purchase DEFERRED. Hard decision deadline: end of W3.
  If not purchased, W4 TLS uses nip.io + Let's Encrypt (skips ACM/Route 53 DNS validation).
  Cost if purchased: ~$14/yr (.com) or ~$4/yr (.click), plus $0.50/mo hosted zone.

## Open items
- ADR 0001: `dev`-as-staging-boundary sentence conflicts with Jenkins design
  (staging deploys from main, not dev). Resolve by W10.

## Cost to date
- $0.00

## Verification (W1D1)
Direct push to main rejected:
    remote: error: GH013: Repository rule violations found for refs/heads/main.
    remote: - Changes must be made through a pull request.
    ! [remote rejected] main -> main (push declined due to repository rule violations)
