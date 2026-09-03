# HireOps

HireOps is a portfolio DevOps project for a small hiring operations platform that will eventually support job descriptions, resume intake, and candidate match scoring. The real purpose of the project is to practice production-style DevOps work in a visible, interview-ready repository: Git workflow, documentation, CI/CD, containers, Kubernetes, infrastructure as code, monitoring, release controls, and operational runbooks.

**Status:** Week 1 — repository foundation

## Stack

- Git

## Repository conventions

This repository uses `main` and `dev` branches, with pull requests for changes going into `main`.

Commits follow Conventional Commits, such as `feat:`, `fix:`, `docs:`, `test:`, and `chore:`.

Production releases will use protected `v*` tags, such as `v1.0.0`.

See [ADR 0001: Branching and Release Strategy](docs/adr/0001-branching-and-release-strategy.md) for the reasoning behind these conventions.

## Documentation

- [Architecture](docs/architecture.md)
- [Progress](docs/PROGRESS.md)
- [ADRs](docs/adr/)
