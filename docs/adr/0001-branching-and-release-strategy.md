# ADR 0001: Branching and Release Strategy

**Status:** Accepted
**Date:** 2026-09-03

## Context

HireOps is a solo portfolio project built over 12 weeks at roughly 10 hours per week. There is no second reviewer, but the history needs disciplined change control because the repo will be used in interviews. The release path must stay simple for Week 1 while leaving a hook for Jenkins or GitHub Actions to trigger staging and production deployments later. The workflow should expose PRs, checks, release tags, and rollback points without pretending to be a full team process.

## Decision

Use `main` for production-ready code and `dev` as the integration branch for unreleased work. All changes into `main` go through PRs from `dev` or short-lived feature branches. Use Conventional Commits, including `feat:`, `fix:`, `docs:`, `test:`, and `chore:`. Mark production releases with protected `v*` tags, such as `v1.0.0`. Set required approvals to `0` because there is no real second reviewer.

## Consequences

Every change to `main` has a reviewable diff and a stable merge point for future required status checks. From Week 9 onward, CI can attach tests, image builds, and deployment checks to the same PR gate. Protected `v*` tags keep the release reference fixed after approval, making the Week 10 production approval meaningful. DORA lead time should be calculated from PR merge time to release tag or deploy time; Conventional Commits only make change types easier to classify.

## What I Gave Up

`dev` adds delay and merge overhead. Trunk-based development would be faster and closer to many high-performing teams. I chose `dev` because this project needs a visible staging boundary for Jenkins, Kubernetes, and interview explanation. The PR gate is procedural, not peer review. Revisit this when a second engineer joins or after two successful tagged production releases with required CI checks.
