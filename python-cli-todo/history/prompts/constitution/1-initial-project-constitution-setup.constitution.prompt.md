---
id: 1
title: Initial project constitution setup
stage: constitution
date: 2025-12-07
surface: agent
model: gemini-1.5-flash
feature: none
branch: unknown
user: user
command: /sp.constitution Hackathon II — Spec-Driven Todo Application
labels: ["constitution", "initial-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
---

## Prompt

This is the Gemini CLI. We are setting up the context for our chat.
Today's date is Sunday, December 7, 2025 (formatted according to the user's locale).
My operating system is: linux
The project's temporary directory is: /home/tonymark/.gemini/tmp/771bf84349b1ba0c4b8171900b6aaa3d557490a9b86252135e33974de0e90331
I'm currently working in the directory: /mnt/d/Projects/hackathon_2_cli_todo_phase_1
Here is the folder structure of the current working directories:

Showing up to 200 items (files + folders). Folders or files indicated with ... contain more items not shown, were ignored, or the display limit (200 items) reached.

/mnt/d/Projects/hackathon_2_cli_todo_phase_1/
├───GEMINI.md
├───.gemini/
│   └───commands/
│       ├───sp.adr.toml
│       ├───sp.analyze.toml
│       ├───sp.checklist.toml
│       ├───sp.clarify.toml
│       ├───sp.constitution.toml
│       ├───sp.git.commit_pr.toml
│       ├───sp.implement.toml
│       ├───sp.phr.toml
│       ├───sp.plan.toml
│       ├───sp.specify.toml
│       └───sp.tasks.toml
├───.specify/
│   ├───memory/
│   │   └───constitution.md
│   ├───scripts/
│   │   └───bash/
│   │       ├───check-prerequisites.sh
│   │       ├───common.sh
│   │       ├───create-adr.sh
│   │       ├───create-new-feature.sh
│   │       ├───create-phr.sh
│   │       ├───setup-plan.sh
│   │       └───update-agent-context.sh
│   └───templates/
│       ├───adr-template.md
│       ├───agent-file-template.md
│       ├───checklist-template.md
│       ├───phr-template.prompt.md
│       ├───plan-template.md
│       ├───spec-template.md
│       └───tasks-template.md
└───venv/
    ├───Include/...
    ├───Lib/...
    └───Scripts/...

Reminder: Do not return an empty response when a tool call is required.

My setup is complete. I will provide my first command in the next turn.---
description: Create or update the project constitution from interactive or provided principle inputs, ensuring all dependent templates stay in sync
---

## User Input

```text
/sp.constitution Hackathon II — Spec-Driven Todo Application

Project Constitution for All Phases (I–V)

🏛️ 1. Purpose of This Constitution

This Constitution defines the rules, governance model, methodology, workflow, responsibilities, and lifecycle for the Spec-Driven Todo Application built for Hackathon II: The Evolution of Todo — Mastering Spec-Driven Development & Cloud-Native AI.
It serves as the foundational document for the entire multi-phase project, covering:
Phase I — In-Memory Console App
Phase II — Full-Stack Web App
Phase III — AI Todo Chatbot (ChatKit + Agents SDK + MCP)
Phase IV — Kubernetes Deployment (Minikube + Helm + AI DevOps)
Phase V — Advanced Cloud-Native Deployment (DOKS/GKE/AKS + Kafka + Dapr)
This Constitution must remain consistent across all phases and governs how the system evolves as specifications grow.

🧭 2. Project Vision

The objective of this project is to simulate the real-world lifecycle of software engineering, evolving a simple CLI Todo app into a distributed, cloud-native, event-driven AI system.
The long-term vision includes:
Adopting Spec-Driven Development as the primary engineering workflow
Using AI-native tools (Claude Code, Spec-Kit Plus, OpenAI Agents SDK, MCP)
Designing an application that can scale from a single file script to a K8s-based multi-service architecture
Mastering modern tools for AI software engineering

📚 3. Core Principles

This project is governed by the following principles:
3.1 Spec-Driven Development (SDD)
All features must be created using:
Specification files under /specs/
Iterative refinement of specs until Claude Code produces correct output
Zero manual code writing

3.2 AI-Native Development

All coding must be done via:
Claude Code or gemini

Spec-Kit Plus

OpenAI Agents SDK

Docker AI (Gordon)

kubectl-ai and kagent
No handwritten implementation is permitted.

3.3 Reproducibility

Every phase must be reproducible from specs alone.
Specifications act as the single source of truth.

3.4 Progressive Evolution

The system must grow phase-by-phase, with each phase building on:
Previous data models
Previous logic
Previous architecture
No phase is isolated — evolution is continuous.

🏗️ 4. Governance Structure
4.1 Specification Authority
All features must originate from:

/specs/overview.md

/specs/features/*.md

/specs/api/*.md

/specs/database/*.md

/specs/ui/*.md

Specs define behavior; code must obey specs.

4.2 Tooling Rules

Claude Code is the only code generator.
Specs must be referenced using @specs/... inside Claude Code.
Specs must be updated before asking for new implementation.

4.3 Change Control

Any major change requires:
Updating the relevant spec file
Running Claude Code to re-generate or update implementation
Committing spec change + implementation change as a pair

4.4 Repository Structure Rules

A monorepo must be used with folders:

/frontend
/backend
/specs
/specs/features
/specs/api
/specs/database
/specs/ui
/.spec-kit
README.md
CONSTITUTION.md
CLAUDE.md

⚙️ 5. Development Workflow

This workflow is mandatory for all phases:

5.1 Write or update the specification

Each new feature must first appear in the appropriate /specs/ file before any code is generated.

5.2 Invoke Claude Code

Use commands like:

“Implement @specs/features/task-crud.md”

“Update backend according to @specs/api/rest-endpoints.md”

5.3 Testing and Validation

Run the application locally

If issues appear → update spec → regenerate code
No manual code edits allowed.

5.4 Documentation

Every phase must include:
README updates
Spec updates
Demo video under 90 seconds
Clear commit history showing SDD workflow

🧩 6. Phase Definitions
6.1 Phase I — In-Memory Python Console App

Build a CLI app with:
Add Task
Delete task
Update Task
View Tasks
Mark Complete
Requirements:
Python 3.13+
UV environment
Spec-Kit Plus
Claude Code or gemini
In-memory data only

6.2 Phase II — Full-Stack Web Application

Tech stack:
Next.js (frontend)
FastAPI (backend)
SQLModel (ORM)
Neon PostgreSQL (database)
Better Auth + JWT (authentication)
Deliverables:
REST API
UI pages
JWT verification middleware
DB schema matching specs

6.3 Phase III — AI Todo Chatbot

Using:
OpenAI ChatKit
OpenAI Agents SDK
Official MCP SDK
FastAPI backend
Neon PostgreSQL
Required:
NLP interface to manage tasks
MCP tools: add, list, update, delete, complete
Stateless chat endpoint
Database-backed conversation logging

6.4 Phase IV — Local Kubernetes Deployment

Using:

Docker containers
Docker AI “Gordon”
Minikube
Helm charts
kubectl-ai
kagent
Application must run on Minikube.

6.5 Phase V — Advanced Cloud Deployment

Cloud provider (choose one):
DigitalOcean Kubernetes (DOKS)
Google GKE
Azure AKS
Added features:
Recurring tasks
Priorities, tags
Search, filter, sort
Due dates + reminders
Infrastructure:
Kafka (Redpanda recommended)
Dapr for:
Pub/Sub
State
Secrets
Cron
Service invocation

🏅 7. Bonus Features Rules

Optional but available for +600 points:
Reusable Intelligence via Claude Code Subagents
Cloud-Native Blueprints
Urdu support
Voice commands
Bonus features require their own specs.

🧪 8. Testing Standards

All phases must be tested for:
Correct implementation of specs
Edge-case handling
Clean error messages
Authentication security
Stateless architecture in Phase III+

🚀 9. Deployment Requirements

Every phase must publish:

Phase II → Vercel + Backend URL

Phase III → Chatbot UI deployed

Phase IV → Local Minikube instructions

Phase V → Live cloud URL



📝 11. Amendments

Any changes to the development methodology or architecture require:

Updating this Constitution

Commit message referencing the amendment

Regenerating affected code

🎯 12. Final Guiding Principles

Specs come first

AI generates code
Manual coding is forbidden
Architecture must evolve progressively
Documentation is part of the grade
Quality matters as much as functionality

🏁 End of Constitution
```

## Response snapshot

The project constitution at `.specify/memory/constitution.md` has been updated to version 1.0.0 with the provided content. A Sync Impact Report detailing changes and affected templates has been added.

**Summary**:
The project constitution at `.specify/memory/constitution.md` has been updated with the content provided by the user. The version has been set to `1.0.0`, with the ratification and last amended dates recorded as 2025-12-07. A Sync Impact Report has been added as an HTML comment at the top of the file, detailing the changes and listing templates that require future updates for consistency.

**Files flagged for manual follow-up**:
*   `.specify/templates/plan-template.md`
*   `.specify/templates/spec-template.md`
*   `.specify/templates/tasks-template.md`
*   All `.toml` files in `.gemini/commands/` (e.g., `sp.adr.toml`, `sp.analyze.toml`, etc.)

**Suggested commit message**:
`docs: Initial project constitution v1.0.0`

## Outcome

- ✅ Impact: Constitution document created/updated successfully.
- 🧪 Tests: No specific tests were run for this constitution update, as it's a documentation task.
- 📁 Files: `.specify/memory/constitution.md` updated.
- 🔁 Next prompts: Review listed templates for consistency updates.
- 🧠 Reflection: Successfully updated the constitution based on user input and generated Sync Impact Report. Handled script failure for PHR creation by falling back to agent-native method.

## Evaluation notes (flywheel)

- Failure modes observed: PHR creation script failed to find template.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: Investigate why `create-phr.sh` couldn't find the template.
