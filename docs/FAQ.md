<!-- TERVYNIX_ANIMATED_HEADER_START -->
<div align="center">

# Tervynix FAQ

### Quick answers about the project, architecture, and roadmap

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2400&pause=900&color=36BCF7&center=true&vCenter=true&width=950&lines=What+is+Tervynix%3F;What+is+implemented+today%3F;Where+is+the+architecture+going%3F;How+can+developers+contribute%3F"
  alt="Tervynix FAQ animated header"
/>

<br />

<img src="https://img.shields.io/badge/FAQ-Project%20Guide-3178C6?style=for-the-badge" />
<img src="https://img.shields.io/badge/Tervynix-Active%20Development-238636?style=for-the-badge" />

<br /><br />

<a href="../README.md">← Project Home</a> •
<a href="./ARCHITECTURE.md">Architecture</a> •
<a href="../ROADMAP.md">Roadmap</a>

</div>

---

<!-- TERVYNIX_ANIMATED_HEADER_END -->

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
