<!-- TERVYNIX_ANIMATED_HEADER_START -->
<div align="center">

# Tervynix Changelog

### Engineering milestones, migrations, and reliability work

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2400&pause=900&color=36BCF7&center=true&vCenter=true&width=950&lines=Track+meaningful+engineering+milestones;Runtime+%E2%80%A2+Persistence+%E2%80%A2+Architecture+%E2%80%A2+Reliability;PostgreSQL+Migration+%E2%80%A2+Runtime+History+%E2%80%A2+Testing;Every+milestone+makes+Tervynix+more+reliable"
  alt="Tervynix Changelog animated header"
/>

<br />

<img src="https://img.shields.io/badge/Changelog-Engineering-3178C6?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Active-238636?style=for-the-badge" />

<br /><br />

<a href="./README.md">← Project Home</a> •
<a href="./docs/ARCHITECTURE.md">Architecture</a> •
<a href="./ROADMAP.md">Roadmap</a>

</div>

---

<!-- TERVYNIX_ANIMATED_HEADER_END -->

All notable engineering milestones and public development updates for Tervynix are documented here.

Tervynix is under active development. This changelog focuses on meaningful product, architecture, runtime, persistence, reliability, and infrastructure milestones rather than every individual commit.

---

## Unreleased

### In Progress

#### PostgreSQL Migration

The broader migration from legacy MongoDB-backed persistence toward PostgreSQL continues.

Current engineering direction includes:

* Repository contracts
* PostgreSQL adapters
* Drizzle ORM integration
* Service-layer database separation
* Real PostgreSQL integration testing
* Incremental migration of remaining persistence domains

#### Backend Modernization

Migration toward the target backend architecture continues:

* TypeScript-first backend
* NestJS
* Fastify
* Domain-oriented services
* Repository abstractions
* Infrastructure adapters
* Clear separation between application and persistence layers

#### Runtime Reliability

Ongoing runtime work includes:

* PTY lifecycle reliability
* Windows ConPTY stability
* Terminal runtime validation
* Process lifecycle hardening
* Runtime acceptance testing

---

## 2026-09-24

### Runtime History PostgreSQL Migration

Completed the scoped PostgreSQL migration and reliability work for Tervynix Runtime History.

#### Added

* PostgreSQL runtime-history repository
* Runtime-history repository contract
* PostgreSQL-specific integration tests
* PostgreSQL acceptance coverage
* Recovery scoping behavior
* Duplicate execution protection
* Retention handling
* Pagination support
* Stable history ordering

#### Updated

* Runtime-history recorder
* MongoDB runtime-history compatibility implementation
* Runtime-history tests
* PostgreSQL history tests
* PostgreSQL acceptance tests

#### Validation

The completed scope passed:

* **History ordering — PASS**
* **Pagination — PASS**
* **Retention — PASS**
* **Duplicate protection — PASS**
* **Recovery scoping — PASS**

Automated verification:

* **22 focused tests passed**
* **8 real PostgreSQL tests passed**
* Targeted TypeScript typecheck passed
* Targeted lint passed

The temporary PostgreSQL instance used for validation was removed after the test run.

#### Recovery Safety

Runtime recovery behavior was changed to be intentionally conservative.

Application startup no longer automatically interrupts historical runtime records.

Recovery now requires explicitly confirmed stopped execution identities before runtime-history state is modified.

This prevents normal application startup from incorrectly changing execution history.

#### Result

**Runtime History PostgreSQL migration and recovery-safety scope: COMPLETE**

No blocker remains for this scoped work.

---

## September 2026

### Public Architecture Documentation

Added public technical documentation describing the architecture and current engineering status of Tervynix.

Added:

* `docs/ARCHITECTURE.md`
* `docs/DEVELOPMENT_STATUS.md`

The architecture documentation distinguishes clearly between:

* Implemented functionality
* Work currently in progress
* Planned infrastructure

This helps prevent future roadmap technologies from being represented as already production-complete.

---

### Developer Workspace Foundation

Established the core Tervynix developer workspace.

Capabilities include:

* Monaco-powered code editor
* Multi-file tabs
* Autosave
* Manual save
* Workspace persistence
* Project workspaces
* Keyboard-driven development workflows

---

### Integrated Terminal Foundation

Built the initial integrated terminal architecture.

Capabilities include:

* Integrated terminal
* Multiple terminal sessions
* Terminal session management
* Terminal reattachment
* Shell process tracking

Terminal and PTY reliability continue to be hardened across supported environments.

---

### Runtime Management Foundation

Established the initial Tervynix runtime-management system.

Capabilities include:

* Process management
* Process start
* Process stop
* Process restart
* Port management
* Runtime monitoring
* Runtime events
* Runtime history
* Task discovery
* Task execution
* Preview and open-port workflows
* Realtime runtime communication

---

### Authentication and Project Protection

Implemented the initial authentication and project ownership foundation.

Capabilities include:

* Authentication
* Login
* Logout
* Authenticated project access
* Project ownership protection

Future authorization work will expand this foundation for teams, collaboration, cloud workspaces, and more advanced permission models.

---

## Architecture Direction

Tervynix is progressively moving toward the following architecture:

### Application

* TypeScript
* React
* Next.js
* Monaco Editor
* xterm.js

### Backend

* NestJS
* Fastify
* Domain services
* Repository contracts
* Infrastructure adapters

### Persistence

* PostgreSQL
* Drizzle ORM

### Realtime and Infrastructure

Planned and evolving infrastructure includes:

* WebSockets
* Redis
* BullMQ

### Runtime

A dedicated Rust runtime agent is planned for performance-sensitive runtime operations.

### Future Platform Areas

The long-term roadmap includes:

* Workspace-aware AI
* Cloud development environments
* Deployment infrastructure
* Collaboration
* Developer APIs
* Extension ecosystem
* Observability
* OpenTelemetry
* Advanced security controls

---

## Changelog Policy

This changelog records significant engineering milestones rather than every source-code change.

An entry should normally be added when Tervynix completes or substantially changes one of the following:

* Major feature
* Architecture migration
* Database migration
* Runtime subsystem
* Reliability milestone
* Security capability
* Public API
* Infrastructure component
* Major test milestone
* Deployment capability
* AI subsystem
* Cloud capability

Small refactors, formatting changes, and routine maintenance do not need individual changelog entries.

---

## Project Status

Tervynix remains under active development.

For more information:

* [Project Overview](./README.md)
* [Vision](./VISION.md)
* [Roadmap](./ROADMAP.md)
* [Architecture](./docs/ARCHITECTURE.md)
* [Development Status](./docs/DEVELOPMENT_STATUS.md)
* [Contributing](./CONTRIBUTING.md)
* [Security](./SECURITY.md)
* [Support](./SUPPORT.md)

---

**Build with Tervynix.**

---

<!-- TERVYNIX_ANIMATED_FOOTER_START -->
<div align="center">

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2200&pause=1200&color=36BCF7&center=true&vCenter=true&width=760&lines=Build+with+Tervynix.;One+workspace.+One+runtime.+One+developer+platform.;Code+%E2%86%92+Run+%E2%86%92+Debug+%E2%86%92+Manage"
  alt="Build with Tervynix"
/>

<br />

<a href="./README.md">← Back to Tervynix</a>

</div>
<!-- TERVYNIX_ANIMATED_FOOTER_END -->
