# HireOps Progress

Last updated: 2026-09-03 (Week 1, Day 2)

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
- [x] AWS budget alarms created ($20 with 80/100 actual + 100 forecasted, $50 with 100 actual)

### W1D2: FastAPI application skeleton
- [x] Python venv (.venv, Python 3.14.4), gitignored
- [x] Dependencies installed and pinned to requirements.txt
- [x] app/main.py with /health, /ready, /jobs, /candidates, /slow
- [x] /health has no external dependencies (liveness semantics)
- [x] /slow uses `await asyncio.sleep(5)` — non-blocking, verified
- [x] Service runs: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`
- [ ] /docs reachable from Windows browser (WSL port forwarding check)

## In progress
- W1D3: docker-compose + Postgres, honest /ready, memory-leak endpoint

## Known gaps (deliberate, scheduled)
- `/ready` returns 200 unconditionally with empty `checks: {}`.
  An always-passing readiness probe is confidently wrong. Fix in D3:
  must return 503 when a dependency check fails, not just a different body.
- Module-level `JOBS = []` / `CANDIDATES = []` is per-process state.
  Will not survive multiple replicas in W7. Postgres in D3 is the fix.
- No response models / type hints yet. Add in D3 when payload shapes are real.
- Deliberate defects: 1 of 3 built.
  - [x] Slow endpoint (`/slow`) — feeds p95 latency SLO, W11 incident
  - [ ] Memory leak endpoint (env-gated) — feeds pod restarts / OOMKilled, W11
  - [ ] Killable external dependency — arrives with Postgres in D3

## Blocked
- (none)

## Decisions
- AWS region: us-east-2
- AWS account: root MFA enabled; IAM admin user NOT yet created (W3 D1)
- Budget alarms: `hireops` ($20: 80/100 actual, 100 forecasted), `hireops-monthly-50` ($50: 100 actual)
- Dependency pinning via `pip freeze`. Direct vs transitive deps are flattened;
  pip-tools/poetry/uv would preserve the distinction. Acceptable at this size.

## Deferred / dropped
- Domain purchase DEFERRED. Hard decision deadline: end of W3.
  If not purchased, W4 TLS uses nip.io + Let's Encrypt (skips ACM/Route 53 DNS validation).
  Cost if purchased: ~$14/yr (.com) or ~$4/yr (.click), plus $0.50/mo hosted zone.

## Open items
- ADR 0001: `dev`-as-staging-boundary sentence conflicts with Jenkins design
  (staging deploys from main, not dev). Resolve by W10.
- Python 3.14.4 is very new. uvloop/httptools compiled fine, but psycopg in D3
  is the real wheel test. If it compiles from source, rebuild venv on 3.12.

## Cost to date
- $0.00

## Verification log

### W1D1 — branch protection enforced
    remote: error: GH013: Repository rule violations found for refs/heads/main.
    remote: - Changes must be made through a pull request.
    ! [remote rejected] main -> main (push declined due to repository rule violations)

### W1D2 — /slow does not block the event loop
    $ curl -s localhost:8000/slow > /dev/null &
    $ sleep 1 && time curl -s localhost:8000/health
    {"status":"ok"}
    real    0m0.008s

    /health returned in 8ms while /slow was in flight.
    Confirms `await asyncio.sleep` yields to the event loop;
    `time.sleep` would have stalled every concurrent request.
