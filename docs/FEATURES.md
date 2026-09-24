# Tervynix Features

This document provides a public overview of the current and planned capabilities of Tervynix.

Tervynix is under active development.

Status meanings:

- ✅ Implemented
- 🟡 In progress / being hardened
- ⚪ Planned

---

## Developer Workspace

### Code Editor

**Status: ✅ Implemented**

Tervynix provides a Monaco-powered development workspace.

Current capabilities include:

- Monaco Editor
- Multi-file editing
- File tabs
- Autosave
- Manual save
- Workspace persistence
- Keyboard-driven workflows

---

## Project Management

**Status: ✅ Implemented**

Current capabilities include:

- Project creation
- Project management
- Authenticated project access
- Project ownership protection
- Workspace configuration

Future project capabilities will expand as cloud workspaces and collaboration are introduced.

---

## Integrated Terminal

**Status: ✅ Implemented / 🟡 hardening**

Tervynix includes an integrated terminal environment.

Current capabilities include:

- Multiple terminal sessions
- Terminal session management
- Terminal reattachment
- Shell process tracking
- xterm.js-based terminal UI
- PTY-backed runtime execution

### Current Engineering Focus

Terminal reliability work continues around:

- PTY lifecycle handling
- Windows ConPTY stability
- Runtime cleanup
- Terminal end-to-end testing

---

## Process Management

**Status: ✅ Implemented**

Developers can manage running development processes from the workspace.

Capabilities include:

- Process discovery
- Start processes
- Stop processes
- Restart processes
- Runtime state tracking
- Process lifecycle integration

---

## Port Management

**Status: ✅ Implemented**

Tervynix can detect and manage development services running on local ports.

Capabilities include:

- Port discovery
- Running-service visibility
- Open-port workflows
- Application preview access

---

## Project Tasks

**Status: ✅ Implemented**

Tervynix supports project task discovery and execution.

This allows developers to work with project-defined commands without constantly switching away from the development workspace.

---

## Runtime Monitoring

**Status: ✅ Implemented foundation**

Runtime monitoring connects processes, terminals, ports, tasks, and runtime events.

Capabilities currently include:

- Runtime events
- Runtime state
- Process lifecycle information
- Realtime runtime communication
- Runtime history

---

## Runtime History

**Status: ✅ Current scoped implementation complete**

Runtime History provides visibility into what happened inside a development environment over time.

Validated capabilities include:

- Stable ordering
- Pagination
- Retention
- Duplicate protection
- Recovery scoping

Latest validation:

```text
22 focused tests passed
8 real PostgreSQL tests passed
Targeted TypeScript typecheck passed
Targeted lint passed
