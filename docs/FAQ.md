# Tervynix FAQ

This document answers common questions about Tervynix, its current development status, architecture, roadmap, public repository, and contribution process.

---

## What is Tervynix?

Tervynix is a modern developer workspace designed to bring the most important parts of software development into one connected environment.

The long-term workflow is:

**Code → Run → Debug → Manage → Collaborate → Deploy**

The goal is to reduce context switching between code editors, terminals, runtime tools, process managers, infrastructure dashboards, AI assistants, and deployment systems.

---

## Is Tervynix finished?

No.

Tervynix is under active development.

Some major foundations are already implemented, including:

- Monaco-powered code workspace
- Project workspaces
- Integrated terminal
- Multiple terminal sessions
- Process management
- Port management
- Task discovery and execution
- Runtime monitoring
- Runtime history
- Authentication
- Project ownership protection
- Realtime runtime communication

Other areas are still being migrated, hardened, or planned.

---

## Is this repository the full Tervynix source code?

This repository is the official public development hub for Tervynix.

It focuses on:

- Product previews
- Architecture documentation
- Development progress
- Roadmap
- Engineering milestones
- Public discussions
- Contribution guidance
- Security and support information

Not every internal Tervynix implementation component is necessarily included in this repository.

---

## Is Tervynix open source?

Tervynix follows the licensing terms defined in:

[LICENSE](../LICENSE)

Public visibility does not automatically mean unrestricted open-source usage.

Review the license before copying, modifying, redistributing, rebranding, or commercially using Tervynix materials.

---

## What technologies does Tervynix use?

### Frontend

- TypeScript
- React
- Next.js
- Monaco Editor
- xterm.js

### Backend Direction

- TypeScript
- NestJS
- Fastify
- Domain services
- Repository contracts
- Infrastructure adapters

### Persistence

- PostgreSQL
- Drizzle ORM

MongoDB remains present in some parts of the architecture during migration.

### Realtime

- WebSockets

Planned infrastructure includes:

- Redis
- BullMQ

### Runtime

Current runtime infrastructure includes Node.js and PTY-based execution.

A Rust runtime agent is planned for future performance-sensitive runtime operations.

---

## Why is Tervynix moving from MongoDB to PostgreSQL?

The migration is intended to improve:

- Relational modeling
- Persistence consistency
- Typed database access
- Repository boundaries
- Testing
- Maintainability
- Long-term scalability

The migration is incremental.

Tervynix is not being completely rewritten just to change databases.

---

## Has PostgreSQL migration started?

Yes.

PostgreSQL migration is already in progress.

Runtime History is one validated migrated area.

Current validated behavior includes:

- History ordering
- Pagination
- Retention
- Duplicate protection
- Recovery scoping

Validation included:

```text
22 focused tests passed
8 real PostgreSQL tests passed
Targeted TypeScript typecheck passed
Targeted lint passed