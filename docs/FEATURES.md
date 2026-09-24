<!-- TERVYNIX_ANIMATED_HEADER_START -->
<div align="center">

# Tervynix Features

### Current capabilities and future platform direction

<img
  src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=24&duration=2400&pause=900&color=36BCF7&center=true&vCenter=true&width=950&lines=Editor+%E2%80%A2+Terminal+%E2%80%A2+Processes+%E2%80%A2+Ports;Runtime+History+%E2%80%A2+Realtime+%E2%80%A2+Authentication;AI+%E2%80%A2+Cloud+%E2%80%A2+Deployment+%E2%80%A2+Collaboration;One+connected+developer+workspace"
  alt="Tervynix Features animated header"
/>

<br />

<img src="https://img.shields.io/badge/Features-Developer%20Platform-3178C6?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Evolving-238636?style=for-the-badge" />

<br /><br />

<a href="../README.md">← Project Home</a> •
<a href="./ARCHITECTURE.md">Architecture</a> •
<a href="../ROADMAP.md">Roadmap</a>

</div>

---

<!-- TERVYNIX_ANIMATED_HEADER_END -->

This document answers common questions about Tervynix, its current development status, architecture, roadmap, and public repository.

---

## What is Tervynix?

Tervynix is a developer workspace being built to bring coding, terminals, runtime management, project workflows, AI-assisted development, and deployment into one connected environment.

The long-term workflow is:

**Code → Run → Debug → Manage → Collaborate → Deploy**

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
- Task execution
- Runtime monitoring
- Runtime history
- Authentication
- Project ownership protection
- Realtime runtime communication

Other parts are still being migrated, hardened, or planned.

---

## Is this repository the full Tervynix source code?

This repository serves as the public development hub for Tervynix.

It focuses on:

- Product information
- Screenshots
- Architecture
- Development progress
- Roadmap
- Engineering milestones
- Public discussions
- Contribution guidance

The availability of this repository does not necessarily mean every internal Tervynix implementation component is publicly distributed here.

---

## Is Tervynix open source?

Tervynix currently uses the licensing terms defined in the repository's [LICENSE](../LICENSE).

Public visibility does not automatically mean unrestricted open-source usage.

Review the license before copying, redistributing, modifying, or commercially using Tervynix materials.

---

## What technology does Tervynix use?

Current and target technologies include:

### Frontend

- TypeScript
- React
- Next.js
- Monaco Editor
- xterm.js

### Backend

- NestJS
- Fastify
- TypeScript
- Domain services
- Repository abstractions

### Persistence

- PostgreSQL
- Drizzle ORM

MongoDB remains present in parts of the architecture during migration.

### Realtime

- WebSockets

Future distributed infrastructure may include:

- Redis
- BullMQ

### Runtime

Current runtime infrastructure includes Node.js and PTY-based execution.

A Rust runtime agent is planned for future performance-sensitive runtime operations.

---

## Why is Tervynix moving from MongoDB to PostgreSQL?

The migration is intended to provide stronger relational modeling, predictable persistence behavior, typed access patterns, and clearer repository boundaries for the growing platform.

The migration is incremental.

Tervynix is not being completely rewritten just to change databases.

---

## Has PostgreSQL migration started?

Yes.

The migration is in progress.

Runtime History is one area where PostgreSQL-backed behavior has already been implemented and validated.

Current validation includes:

- History ordering
- Pagination
- Retention
- Duplicate protection
- Recovery scoping

The validated scope passed:

- 22 focused tests
- 8 real PostgreSQL tests
- Targeted TypeScript typecheck
- Targeted lint

---

## Why does Tervynix use repository contracts?

Repository contracts separate application behavior from database implementations.

Instead of application services depending directly on PostgreSQL or MongoDB, they can depend on an interface or contract.

This makes migrations, testing, and future infrastructure changes safer and easier to reason about.

---

## Is NestJS already fully migrated?

No.

The NestJS and Fastify backend architecture is still being introduced incrementally.

The objective is to move toward clearer domain boundaries without unnecessarily rebuilding working application behavior.

---

## Is Redis already implemented?

Not as a production-complete Tervynix subsystem.

Redis is part of the planned distributed infrastructure direction.

Potential uses include:

- Realtime coordination
- Cross-instance communication
- Distributed state
- Caching where appropriate

---

## Is BullMQ implemented?

Not yet as a completed subsystem.

BullMQ is planned for background processing such as:

- Long-running jobs
- Deployment tasks
- Workspace maintenance
- Infrastructure operations
- AI-related background work

---

## Does Tervynix use Rust?

A dedicated Rust runtime agent is planned.

The future Rust layer may handle:

- Process management
- Process-tree discovery
- Signals
- PTY operations
- Port discovery
- File-system monitoring
- Runtime metrics
- Resource monitoring

The Rust agent is intended to operate behind a runtime abstraction.

---

## Does Tervynix already have AI features?

AI-assisted development is part of the long-term platform direction.

Planned capabilities include:

- Repository-aware assistance
- Workspace context
- Code generation
- Code explanation
- Refactoring
- Debugging
- Multi-file understanding
- Runtime-aware debugging
- Code review
- Documentation generation

Planned AI features should not be interpreted as production-complete functionality.

---

## Will Tervynix support cloud development environments?

That is part of the long-term roadmap.

Possible capabilities include:

- Cloud workspaces
- Remote runtime execution
- Persistent sessions
- Remote terminals
- Workspace synchronization
- Resume and reconnect workflows
- Application previews

---

## Will Tervynix support deployment?

Deployment is part of the planned platform direction.

Future capabilities may include:

- Project deployment
- Environment configuration
- Deployment logs
- Deployment status
- Domain integration
- Runtime monitoring

---

## What is Runtime History?

Runtime History records important information about execution activity inside a Tervynix workspace.

It is designed to help developers understand what happened previously during runtime operations.

Current validated behavior includes:

- Stable ordering
- Pagination
- Retention
- Duplicate protection
- Recovery scoping

---

## What does recovery scoping mean?

Tervynix avoids automatically assuming that historical execution records should be marked as interrupted during application startup.

Recovery requires explicitly confirmed stopped execution identities.

This helps protect runtime history from incorrect state changes.

---

## Why is Windows PTY / ConPTY mentioned in the documentation?

Tervynix includes integrated terminal functionality, and PTY behavior can vary across operating systems.

Windows ConPTY reliability is therefore treated as a dedicated engineering and testing concern rather than hidden as a generic terminal issue.

---

## Can I contribute to Tervynix?

Yes, public feedback and appropriate contributions are welcome.

Before contributing, read:

- [CONTRIBUTING.md](../CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md)
- [SECURITY.md](../SECURITY.md)
- [LICENSE](../LICENSE)

---

## How do I report a bug?

Use the GitHub Bug Report issue template.

Please include:

- Operating system
- Environment information
- Steps to reproduce
- Expected behavior
- Actual behavior
- Relevant logs
- Screenshots where useful

Never include passwords, access tokens, API keys, private repository content, or database credentials.

---

## How do I suggest a feature?

Use the GitHub Feature Request template.

A useful feature proposal should explain:

1. The developer problem
2. The current limitation
3. The desired outcome
4. A possible solution
5. Any important technical considerations

---

## Can I submit a pull request?

Yes, subject to the project's contribution and licensing requirements.

The repository includes a pull request template to help contributors document:

- Purpose
- Implementation details
- Testing
- Database impact
- Runtime impact
- Security impact
- Backward compatibility

---

## Where can I see what is being worked on?

See:

- [Development Status](./DEVELOPMENT_STATUS.md)
- [Roadmap](../ROADMAP.md)
- [Changelog](../CHANGELOG.md)

---

## Where can I understand the architecture?

See:

- [Architecture](./ARCHITECTURE.md)
- [Features](./FEATURES.md)
- [Vision](../VISION.md)

---

## Can I sponsor or support Tervynix?

Formal sponsorship options may be added later.

For now, useful ways to support the project include:

- Star the repository
- Follow development
- Share constructive feedback
- Report reproducible bugs
- Suggest well-defined features
- Participate in GitHub Discussions

---

## Is the roadmap guaranteed?

No.

The roadmap represents the current direction of Tervynix.

Priorities may change based on:

- Engineering findings
- Reliability requirements
- Security requirements
- Testing results
- Platform constraints
- User feedback
- Product direction

---

## Where should I start?

If you are new to Tervynix, read these in order:

1. [README](../README.md)
2. [Features](./FEATURES.md)
3. [Development Status](./DEVELOPMENT_STATUS.md)
4. [Roadmap](../ROADMAP.md)
5. [Architecture](./ARCHITECTURE.md)
6. [Vision](../VISION.md)

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

<a href="../README.md">← Back to Tervynix</a>

</div>
<!-- TERVYNIX_ANIMATED_FOOTER_END -->
