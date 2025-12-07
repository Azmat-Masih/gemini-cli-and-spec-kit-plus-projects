# Feature Specification: Phase I In-Memory Python Console Todo Application

**Feature Branch**: `001-phase1-console-todo`  
**Created**: 2025-12-07  
**Status**: Draft  
**Input**: User description: "Phase I — In-Memory Python Console Todo Application Specification Document (Spec-Driven Development) 🧩 1. Phase Overview Phase I represents the foundation of the multi-phase Todo Application. The objective is to build a fully functional, in-memory Python console app that implements all Basic Level features using Spec-Driven Development (SDD) This phase establishes: The initial data model Core task operations Project structure Spec-driven workflow AI-assisted coding practices No backend, no frontend UI, no database, and no cloud deployment are included in this phase. 🎯 2. Goals of Phase I Build a stable console-based Todo application Implement complete CRUD functionality Use only in-memory data storage Follow strict Spec-Driven Development workflows Generate all code through an AI coding agent (Claude, Gemini, or any allowed model) Create a clean and organized Python project structure This phase is the foundation for later phases where the app evolves into full-stack and cloud-native architecture. 📌 3. Scope of Phase I Included Features (Required) You must implement all 5 Basic Level Todo requirements: Add Task Create a new todo item with title and optional description. View Tasks Display a list of all tasks with ID, title, and completion status. Update Task Modify title and/or description of an existing task. Delete Task Remove an existing task by its ID. Mark as Complete Toggle task completion on/off. 🚫 Not Included in Phase I The following features and technologies MUST NOT be used in Phase 1: No Next.js No FastAPI No SQLModel No Neon PostgreSQL No Authentication No Chat interface No OpenAI Agents / MCP No Kubernetes No Kafka No Dapr No reminders, recurring tasks, search, tags, priorities, sorting, or filters These belong to later phases and are intentionally excluded here. 🛠️ 4. Functional Requirements 4.1 Task Model A task must contain: id: integer (auto-increment) title: string (required, 1–200 chars) description: string (optional, max 1000 chars) completed: boolean (default: False) 4.2 Console UI Requirements Must be fully operable via text-based menu Provide clear instructions to the user Input validation must be implemented Must support repeated operations without restarting the program 4.3 Task Operations Details Add Task Validate title Assign incremental ID Save task in memory View Tasks Show ID, title, status Show “No tasks found” if list is empty Update Task Must allow updating title and/or description Should prevent updating non-existent IDs Delete Task Should confirm removal via user action Should handle invalid IDs gracefully Mark Complete / Incomplete Toggle boolean value Provide feedback after action ⚙️ 5. Non-Functional Requirements Code style must follow Python best practices Run on Python 3.13+ Must use a clean folder structure: /src /app main.py models.py services.py utils.py README.md CONSTITUTION.md All code must be AI-generated, not manually written Specs must be referenced during code generation Changes in logic must be reflected in the spec file first 📄 6. Deliverables for Phase I 1. Console Application (Python) Fully functioning Todo CLI app In-memory data storage 2. GitHub Repository containing: /src folder CONSTITUTION.md specify.md (this file) plan.md tasks.md implement.md README.md with setup/run instructions /specs folder (if using Spec-Kit) 3. Demo Video (90 seconds or less) 🧪 7. Acceptance Criteria A Phase I submission is considered complete when: All 5 features work correctly No crashes occur from invalid input All code was produced using AI (Claude, Gemini, or equivalent) The program runs repeatedly without restarting Repo is clean, organized, and includes required documentation 🔒 8. Constraints NO manual code-writing NO external database NO GUI or Web UI NO external libraries (unless in standard Python library) Only AI-generated, spec-driven code is allowed 🤖 9. About Using Gemini Instead of Claude The official rule is: “You cannot write code manually. You must refine the spec until the AI model generates the correct output.” This means: ✔ You can use Gemini instead of Claude Code as long as: It generates all the code You follow the same spec-driven workflow You do not write implementation manually So yes — Gemini is acceptable and allowed if you do not have access to Claude Code."

## User Scenarios & Testing

### User Story 1 - Add Task (Priority: P1)

The user wants to create a new todo item by providing a title and an optional description. The system should assign a unique ID and store it in memory.

**Why this priority**: Core functionality for any Todo application. Without adding tasks, other features are irrelevant.

**Independent Test**: Can be fully tested by adding a task and then viewing tasks.

**Acceptance Scenarios**:

1.  **Given** the application is running, **When** the user selects "Add Task" and provides a title and optional description, **Then** the task is added to the in-memory list and displayed upon viewing.
2.  **Given** the application is running, **When** the user selects "Add Task" and provides an invalid title (e.g., too long or empty), **Then** an error message is displayed, and the task is not added.

---

### User Story 2 - View Tasks (Priority: P1)

The user wants to see a list of all existing todo tasks, including their ID, title, and completion status.

**Why this priority**: Essential for seeing the state of the Todo list and verifying other operations.

**Independent Test**: Can be fully tested by adding a few tasks and then selecting "View Tasks".

**Acceptance Scenarios**:

1.  **Given** the application is running and tasks exist, **When** the user selects "View Tasks", **Then** a list of all tasks with ID, title, and completion status is displayed.
2.  **Given** the application is running and no tasks exist, **When** the user selects "View Tasks", **Then** a "No tasks found" message is displayed.

---

### User Story 3 - Update Task (Priority: P2)

The user wants to modify the title and/or description of an existing task identified by its unique ID.

**Why this priority**: Important for managing existing tasks and correcting information.

**Independent Test**: Can be fully tested by adding a task, then updating its title/description, and verifying the change by viewing tasks.

**Acceptance Scenarios**:

1.  **Given** a task with a specific ID exists, **When** the user selects "Update Task", provides the ID, and new title/description, **Then** the task's details are updated, and confirmation is provided.
2.  **Given** no task exists with the provided ID, **When** the user attempts to update a non-existent task, **Then** an error message indicating the task was not found is displayed.

---

### User Story 4 - Delete Task (Priority: P2)

The user wants to permanently remove an existing task from the list using its unique ID, with a confirmation step.

**Why this priority**: Allows users to remove completed or unwanted tasks, keeping the list clean.

**Independent Test**: Can be fully tested by adding a task, deleting it, and then verifying its removal by viewing tasks.

**Acceptance Scenarios**:

1.  **Given** a task with a specific ID exists, **When** the user selects "Delete Task", provides the ID, and confirms removal, **Then** the task is removed from the in-memory list, and confirmation is provided.
2.  **Given** no task exists with the provided ID, **When** the user attempts to delete a non-existent task, **Then** an error message indicating the task was not found is displayed.

---

### User Story 5 - Mark as Complete / Incomplete (Priority: P2)

The user wants to change the completion status of an existing task (from incomplete to complete, or vice-versa) using its unique ID.

**Why this priority**: Crucial for tracking task progress and completion.

**Independent Test**: Can be fully tested by adding a task, marking it complete, viewing its status, then marking it incomplete and viewing its status again.

**Acceptance Scenarios**:

1.  **Given** a task with a specific ID exists, **When** the user selects "Mark Complete" (or "Mark Incomplete") and provides the ID, **Then** the task's completion status is toggled, and feedback is provided.
2.  **Given** no task exists with the provided ID, **When** the user attempts to mark complete/incomplete a non-existent task, **Then** an error message indicating the task was not found is displayed.

### Edge Cases

-   What happens when a title is empty or exceeds the maximum length during task creation? (The system should validate the input and display an error message.)
-   How does the system handle non-integer, negative, or non-existent IDs for update, delete, or mark complete operations? (The system should gracefully handle invalid input and provide appropriate feedback to the user.)
-   What happens when the in-memory task list is empty and the user attempts operations like update, delete, or mark complete? (The system should provide appropriate feedback, such as "No tasks to update/delete/mark complete.")

## Requirements

### Functional Requirements

-   **FR-001**: System MUST allow users to add a new todo item with a title (required, 1-200 chars) and an optional description (max 1000 chars).
-   **FR-002**: System MUST assign a unique, auto-incrementing integer ID to each new task.
-   **FR-003**: System MUST store tasks in memory throughout the application's runtime.
-   **FR-004**: System MUST display a list of all tasks, including their ID, title, and completion status. If the list is empty, a "No tasks found" message MUST be displayed.
-   **FR-005**: System MUST allow users to update the title and/or description of an existing task by its ID.
-   **FR-006**: System MUST allow users to delete an existing task by its ID, requiring explicit user confirmation.
-   **FR-007**: System MUST allow users to toggle the completion status of a task by its ID (mark as complete or incomplete).
-   **FR-008**: System MUST provide a text-based menu for all user interactions.
-   **FR-009**: System MUST validate user input for task creation (title length, required fields) and task operations (valid ID format, existence of task).
-   **FR-010**: System MUST provide clear instructions and concise feedback to the user after each operation.
-   **FR-011**: System MUST support repeated operations within a single program execution without requiring a restart.

### Key Entities

-   **Task**: Represents a single todo item.
    *   `id`: Unique integer identifier (auto-incremented).
    *   `title`: String representing the task's title (required, 1-200 characters).
    *   `description`: String representing the task's description (optional, max 1000 characters).
    *   `completed`: Boolean indicating the completion status (default: False).

## Success Criteria

### Measurable Outcomes

-   **SC-001**: All 5 basic CRUD operations (Add, View, Update, Delete, Mark Complete) are fully functional and accessible via the console menu without errors or crashes.
-   **SC-002**: The application handles all specified invalid user inputs gracefully, providing informative and user-friendly error messages.
-   **SC-003**: The application maintains task data in memory accurately, reflecting all additions, updates, deletions, and status changes throughout a single user session.
-   **SC-004**: The console user interface is intuitive, enabling a first-time user to perform all core operations successfully within 5 minutes of launching the application.
-   **SC-005**: All output displays tasks with correct ID, title, and completion status formatting.
