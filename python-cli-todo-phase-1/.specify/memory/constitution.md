<!--
<Sync Impact Report>
<Version Change>: 1.0.0 -> 1.1.0
<Modified Principles>:
    - 3.5 Self-Healing Templates (New)
    - 4.5 Template Management (New)
    - 5.5 Automation Self-Healing (New)
<Added Sections>: None
<Removed Sections>: None
<Templates Requiring Updates>:
    - .specify/templates/plan-template.md (⚠ pending)
    - .specify/templates/spec-template.md (⚠ pending)
    - .specify/templates/tasks-template.md (⚠ pending)
    - .gemini/commands/sp.adr.toml (⚠ pending)
    - .gemini/commands/sp.analyze.toml (⚠ pending)
    - .gemini/commands/sp.checklist.toml (⚠ pending)
    - .gemini/commands/sp.clarify.toml (⚠ pending)
    - .gemini/commands/sp.constitution.toml (⚠ pending)
    - .gemini/commands/sp.git.commit_pr.toml (⚠ pending)
    - .gemini/commands/sp.implement.toml (⚠ pending)
    - .gemini/commands/sp.phr.toml (⚠ pending)
    - .gemini/commands/sp.plan.toml (⚠ pending)
    - .gemini/commands/sp.specify.toml (⚠ pending)
    - .gemini/commands/sp.tasks.toml (⚠ pending)
<Follow-up TODOs>: None
</Sync Impact Report>
-->
# Hackathon II — Spec-Driven Todo Application
Project Constitution for All Phases (I–V)

🏛️ 1. Purpose of This Constitution

This Constitution defines the rules, governance, methodology, workflow, responsibilities, and lifecycle for the Spec-Driven Todo Application built for Hackathon II: The Evolution of Todo — Mastering Spec-Driven Development & Cloud-Native AI.
It covers all phases:
Phase I — In-Memory Console App
Phase II — Full-Stack Web App
Phase III — AI Todo Chatbot (ChatKit + Agents SDK + MCP)
Phase IV — Kubernetes Deployment (Minikube + Helm + AI DevOps)
Phase V — Advanced Cloud-Native Deployment (DOKS/GKE/AKS + Kafka + Dapr)
This Constitution ensures consistent evolution across phases and defines rules to prevent automation failures, such as missing templates.

🧭 2. Project Vision
Evolve a simple CLI Todo app into a distributed, cloud-native, event-driven AI system.
Adopt Spec-Driven Development (SDD) as the core workflow.
Use AI-native tools like Claude Code, Spec-Kit Plus, OpenAI Agents SDK, MCP.
Ensure scalability from single-file scripts to Kubernetes-based multi-service architecture.
Master modern AI software engineering tools while maintaining reproducibility.

📚 3. Core Principles

3.1 Spec-Driven Development (SDD)

All features must originate from specification files under /specs/.
Iteratively refine specs until automated tools produce correct outputs.
No manual code writing is allowed.

3.2 AI-Native Development

Code generation via:
Claude Code
Gemini
Spec-Kit Plus
OpenAI Agents SDK
Docker AI (Gordon)
kubectl-ai and kagent
Manual implementations are prohibited.

3.3 Reproducibility

Every phase must be reproducible from specs alone.
Specifications serve as the single source of truth.

3.4 Progressive Evolution

System evolves phase-by-phase:
Preserves previous data models, logic, and architecture
No phase is isolated

3.5 Self-Healing Templates (New)

Before running automation scripts (PHR generation, MCP commands), all required templates are verified.
Missing templates are automatically created with default placeholders, preventing ENOENT errors.

🏗️ 4. Governance Structure

4.1 Specification Authority
All features originate from:

/specs/overview.md
/specs/features/*.md
/specs/api/*.md
/specs/database/*.md
/specs/ui/*.md


4.2 Tooling Rules

Claude Code is the primary code generator.
Specs must be referenced using @specs/... in commands.
Update specs before requesting new implementation.

4.3 Change Control

Major changes require:
Updating the relevant spec
Regenerating code via AI tools
Committing spec + implementation changes as a pair

4.4 Repository Structure Rules

Monorepo layout:

/frontend
/backend
/specs
/specs/features
/specs/api
/specs/database
/specs/ui
/.spec-kit
/.specify/memory/constitution.md
README.md
CONSTITUTION.md
CLAUDE.md


4.5 Template Management (New)

Maintain a list of required templates (from .specify/templates/ and .gemini/commands/).
Automation scripts check for missing templates and auto-create placeholders before execution.

⚙️ 5. Development Workflow

5.1 Write/Update Specification

All features must first appear in /specs/ before code generation.

5.2 Invoke AI Tools

Example commands:

Implement @specs/features/task-crud.md
Update backend according to @specs/api/rest-endpoints.md


5.3 Test and Validate

Run locally
If issues appear → update spec → regenerate code
No manual edits allowed

5.4 Documentation

Update README
Update specs
Maintain clear commit history

5.5 Automation Self-Healing (New)

Before any PHR/MCP command:
Check required templates exist
Auto-create missing templates with default content
Log created placeholders for review

🧩 6. Phase Definitions

6.1 Phase I — In-Memory Python Console App

CLI tasks: add, delete, update, view, mark complete
Requirements: Python 3.13+, UV environment, Spec-Kit Plus, Claude Code/Gemini

6.2 Phase II — Full-Stack Web Application

Tech: Next.js (frontend), FastAPI (backend), SQLModel, Neon PostgreSQL, JWT auth
Deliverables: REST API, UI, DB schema

6.3 Phase III — AI Todo Chatbot

Tech: ChatKit, OpenAI Agents SDK, MCP, FastAPI, Neon PostgreSQL
Features: NLP interface, MCP task management, stateless chat, DB-backed logs

6.4 Phase IV — Local Kubernetes Deployment

Tech: Docker, Docker AI “Gordon”, Minikube, Helm, kubectl-ai, kagent
Must run on Minikube

6.5 Phase V — Advanced Cloud Deployment

Cloud: DOKS / GKE / AKS
Added: recurring tasks, priorities, tags, search/filter, reminders
Infrastructure: Kafka (Redpanda recommended), Dapr for Pub/Sub, State, Secrets, Cron, Service invocation

🏅 7. Bonus Features Rules

Optional (+600 points):

Reusable Intelligence via Claude Code Subagents
Cloud-native blueprints
Urdu support
Voice commands
Must have dedicated specs

🧪 8. Testing Standards

Validate all phases for:
Correct spec implementation
Edge-case handling
Clean error messages
Authentication security
Stateless architecture in Phase III+

🚀 9. Deployment Requirements

Phase II → Vercel + backend URL

Phase III → Chatbot UI deployed

Phase IV → Minikube instructions

Phase V → Live cloud URL

📝 11. Amendments

Changes to methodology/architecture require:
Updating Constitution
Commit message referencing amendment
Regenerating affected code

🎯 12. Final Guiding Principles

Specs first

AI generates code
Manual coding forbidden
Progressive architecture evolution
Documentation matters as much as functionality
Self-healing automation prevents template-related errors

**Version**: 1.1.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07