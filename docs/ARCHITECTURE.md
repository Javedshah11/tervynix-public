<!-- TERVYNIX_ANIMATED_HEADER_START -->
<div align="center">

# Tervynix Architecture

### Workspace → Services → Persistence → Runtime Infrastructure

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2400&pause=900&color=36BCF7&center=true&vCenter=true&width=950&lines=Next.js+%E2%86%92+NestJS+%2F+Fastify+%E2%86%92+Domain+Services;PostgreSQL+%2B+Drizzle+%E2%80%A2+WebSockets;Redis+%E2%80%A2+BullMQ+%E2%80%A2+Rust+Runtime+Agent;Migrate.+Validate.+Keep+the+platform+operational."
  alt="Tervynix Architecture animated header"
/>

<br />

<img src="https://img.shields.io/badge/Architecture-Modular-3178C6?style=for-the-badge" />
<img src="https://img.shields.io/badge/Migration-Incremental-238636?style=for-the-badge" />

<br /><br />

<a href="../README.md">← Project Home</a> •
<a href="./ARCHITECTURE.md">Architecture</a> •
<a href="../ROADMAP.md">Roadmap</a>

</div>

---

<!-- TERVYNIX_ANIMATED_HEADER_END -->

This document describes the public high-level architecture and engineering direction of Tervynix.

Tervynix is under active development. The architecture is being migrated incrementally so the platform remains operational while major backend, persistence, realtime, and runtime components evolve.

> Status labels used in this document:
>
> * **Implemented** — available in the current product/codebase.
> * **In progress** — actively being migrated, hardened, or integrated.
> * **Planned** — part of the intended architecture but not yet complete.

---

## 1. System Overview

Tervynix is designed as an integrated developer workspace where developers can:

**Code → Run → Debug → Manage → Collaborate → Deploy**

At a high level, the platform is divided into five major areas:

1. Web application and developer workspace
2. Backend application and domain services
3. Persistence and infrastructure
4. Runtime and terminal systems
5. Future AI, cloud, and deployment services

```text
                         TERVYNIX
                            │
             ┌──────────────┴──────────────┐
             │                             │
       Web Application                Backend/API
     React + Next.js                NestJS + Fastify
             │                             │
             │                    Domain / Application
             │                         Services
             │                             │
     Developer Workspace        ┌──────────┼──────────┐
             │                  │          │          │
    ┌────────┼────────┐     PostgreSQL   Redis     BullMQ
    │        │        │      + Drizzle  (Planned)  (Planned)
 Monaco   Terminal   Runtime
 Editor   / xterm    Controls
                      │
                 Runtime Layer
                      │
              Rust Runtime Agent
                   (Planned)
```

This diagram represents the architectural direction rather than claiming every component is already production-complete.

---

## 2. Web Application

**Status: Implemented and evolving**

The primary Tervynix user interface is built with React and Next.js.

Current responsibilities include:

* Authentication flows
* Project management
* Developer dashboard
* Code workspace
* Multi-file tab handling
* Workspace state
* Integrated terminal UI
* Process management UI
* Port management UI
* Task execution
* Runtime monitoring
* Runtime history views
* Realtime runtime updates

### Editor

Tervynix uses Monaco Editor for the development workspace.

Current capabilities include:

* Multi-file editing
* File tabs
* Autosave
* Manual save
* Workspace persistence
* Keyboard-driven editing workflows

### Terminal

The terminal experience is built around xterm.js and PTY-backed runtime sessions.

Current capabilities include:

* Integrated terminal
* Multiple terminal sessions
* Terminal reattachment
* Shell process tracking
* Runtime lifecycle integration

Windows PTY / ConPTY reliability continues to be treated as a dedicated engineering concern.

---

## 3. Backend Architecture

**Status: In progress**

Tervynix is moving toward a TypeScript-first modular backend architecture using:

* NestJS
* Fastify
* Explicit domain boundaries
* Service-layer abstractions
* Repository contracts
* Infrastructure adapters

The migration is intentionally incremental rather than a full rewrite.

The main goal is to separate application behavior from storage and runtime implementation details so services can evolve without tightly coupling business logic to MongoDB, PostgreSQL, PTY implementations, or future infrastructure.

### Intended Backend Shape

```text
Controller / Transport
        │
        ▼
Application / Domain Service
        │
        ▼
Repository / Runtime Contract
        │
        ├──────── PostgreSQL Adapter
        ├──────── MongoDB Adapter
        ├──────── Realtime Adapter
        └──────── Runtime Adapter
```

---

## 4. Persistence

### PostgreSQL

**Status: In progress, with validated migrated areas**

PostgreSQL is the target primary relational datastore.

The migration uses repository abstractions so PostgreSQL-backed implementations can be introduced without forcing all application logic to change at once.

Validated work currently includes PostgreSQL-backed runtime history behavior with coverage for:

* Ordering
* Pagination
* Retention
* Duplicate protection
* Recovery scoping

The runtime-history PostgreSQL work has passed focused automated validation, including real PostgreSQL integration tests.

### Drizzle ORM

**Status: In progress**

Drizzle ORM is part of the target PostgreSQL data-access architecture.

The goal is to provide:

* Typed schema access
* Explicit migrations
* Predictable SQL behavior
* Strong TypeScript integration
* Maintainable repository adapters

### MongoDB

**Status: Legacy / migration source**

MongoDB remains present in parts of the existing architecture while the system transitions toward PostgreSQL-backed persistence.

The migration strategy is to replace storage dependencies behind contracts rather than rebuild unrelated product behavior.

---

## 5. Runtime System

**Status: Implemented foundation, actively hardened**

Runtime management is one of the core parts of Tervynix.

Current runtime capabilities include:

* Process management
* Process start/stop/restart
* Port discovery and management
* Project task discovery
* Task execution
* Terminal sessions
* Runtime events
* Runtime monitoring
* Runtime history
* Realtime runtime communication

### Runtime History

Runtime history records execution events and state transitions so developers can understand what happened inside a workspace over time.

Current validated behavior includes:

* Stable history ordering
* Pagination
* Retention
* Duplicate prevention
* Recovery scoping

Recovery is deliberately conservative: startup does not automatically interrupt historical records.

Recovery requires explicitly confirmed stopped execution identities.

This reduces the risk of corrupting runtime history during ordinary application startup.

---

## 6. Realtime Architecture

**Status: Implemented foundation, expanding**

Tervynix already uses realtime communication for runtime updates.

The target direction includes:

* WebSockets for client/runtime communication
* Distributed event propagation
* Runtime state synchronization
* Multi-instance coordination

### Redis

**Status: Planned**

Redis is intended to support:

* Distributed coordination
* Caching
* Realtime infrastructure
* Cross-instance state

### BullMQ

**Status: Planned**

BullMQ is intended for reliable asynchronous and background work such as:

* Long-running development tasks
* Deployment jobs
* Workspace maintenance
* AI background processing
* Infrastructure operations

---

## 7. Rust Runtime Agent

**Status: Planned**

A dedicated Rust runtime agent is planned for performance-sensitive and operating-system-level runtime operations.

Potential responsibilities include:

* Process management
* Process-tree discovery
* Signal handling
* PTY operations
* Port discovery
* File-system watching
* Runtime metrics
* Resource monitoring

The Rust agent is intended to sit behind a runtime abstraction so the application is not tightly coupled to one runtime implementation.

---

## 8. AI Architecture

**Status: Planned**

Tervynix AI is intended to be workspace-aware rather than a disconnected chat layer.

Planned capabilities include:

* Repository-aware assistance
* Code explanation
* Code generation
* Refactoring
* Debugging assistance
* Multi-file understanding
* Runtime-aware debugging
* Architecture assistance
* Documentation generation
* Automated development tasks

The target architecture will keep AI-provider integrations behind explicit abstractions so providers and models can evolve independently from the rest of the application.

---

## 9. Cloud and Deployment

**Status: Planned**

Long-term Tervynix architecture is intended to support remote and cloud development environments.

Planned capabilities include:

* Cloud workspaces
* Persistent remote sessions
* Remote runtimes
* Workspace synchronization
* Deployment pipelines
* Environment management
* Deployment logs
* Domain integration
* Deployment status monitoring

---

## 10. Security Boundaries

**Status: Implemented foundation, ongoing hardening**

Security-related areas include:

* Authentication
* Project ownership protection
* Authenticated project access
* Backend authorization boundaries
* Runtime isolation
* Credential protection
* Auditability

Future hardening is expected to include:

* Advanced authorization
* Rate limiting
* Audit logs
* Security-focused observability
* Stronger service isolation

See [SECURITY.md](../SECURITY.md) for the public security policy.

---

## 11. Observability

**Status: Planned / partially prepared**

The architecture is intended to support:

* Structured logging
* Runtime metrics
* Distributed tracing
* OpenTelemetry
* Error correlation
* Health checks
* Audit logs

Observability will become increasingly important as Tervynix moves from a single development environment toward distributed runtime and cloud infrastructure.

---

## 12. Migration Principles

Tervynix follows several rules while the architecture evolves:

1. **Migrate, do not blindly rewrite.**
2. **Keep the platform operational after each migration phase.**
3. **Place contracts between application logic and infrastructure.**
4. **Validate migrated behavior with focused tests.**
5. **Do not remove legacy implementations before replacement behavior is verified.**
6. **Treat runtime correctness and recovery safety as first-class concerns.**
7. **Keep planned architecture clearly separated from implemented functionality.**

---

## 13. Current Technology Direction

| Area               | Technology                               | Status                  |
| ------------------ | ---------------------------------------- | ----------------------- |
| Frontend           | React / Next.js                          | Implemented             |
| Language           | TypeScript                               | Implemented / expanding |
| Editor             | Monaco Editor                            | Implemented             |
| Terminal UI        | xterm.js                                 | Implemented             |
| Backend            | NestJS                                   | In progress             |
| HTTP adapter       | Fastify                                  | In progress             |
| Primary database   | PostgreSQL                               | In progress             |
| ORM                | Drizzle ORM                              | In progress             |
| Legacy persistence | MongoDB                                  | Migration source        |
| Realtime           | WebSockets                               | Implemented foundation  |
| Distributed state  | Redis                                    | Planned                 |
| Background jobs    | BullMQ                                   | Planned                 |
| Runtime agent      | Rust                                     | Planned                 |
| Observability      | OpenTelemetry                            | Planned                 |
| AI layer           | Provider abstraction + workspace context | Planned                 |

---

## 14. Architectural Goal

The architectural goal is not simply to build another browser-based editor.

Tervynix is being designed as a complete developer platform where editing, terminals, processes, runtimes, history, AI, infrastructure, and deployment can operate as parts of one connected system.

The architecture will continue to evolve as implementation, testing, and real-world usage expose better design decisions.

---

<!-- TERVYNIX_ANIMATED_FOOTER_START -->
<div align="center">

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=18&duration=2200&pause=1200&color=36BCF7&center=true&vCenter=true&width=760&lines=Build+with+Tervynix.;One+workspace.+One+runtime.+One+developer+platform.;Code+%E2%86%92+Run+%E2%86%92+Debug+%E2%86%92+Manage"
  alt="Build with Tervynix"
/>

<br />

<a href="../README.md">← Back to Tervynix</a>

</div>
<!-- TERVYNIX_ANIMATED_FOOTER_END -->
