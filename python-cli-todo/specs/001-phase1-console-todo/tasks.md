# Tasks: Phase I In-Memory Python Console Todo Application

**Input**: Design documents from `specs/001-phase1-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, quickstart.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

-   **[P]**: Can run in parallel (different files, no dependencies)
-   **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
-   Include exact file paths in descriptions

## Path Conventions

-   **Single project**: `src/`, `tests/` at repository root
-   **Web app**: `backend/src/`, `frontend/src/`
-   **Mobile**: `api/src/`, `ios/src/` or `android/src/`
-   Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure as defined in `plan.md`.

- [X] T001 Create project root folder structure src/app/ src/tests/ specs/ history/
- [X] T002 Create empty file src/app/main.py
- [X] T003 Create empty file src/app/models.py
- [X] T004 Create empty file src/app/services.py
- [X] T005 Create empty file src/app/utils.py
- [X] T006 Update .gitignore to ignore .venv and other generated files (if applicable)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core components that are shared across multiple user stories (Task model, in-memory storage, basic validation helpers).

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Create the Task model in src/app/models.py based on `data-model.md`
- [X] T008 Initialize in-memory storage (e.g., a Python list for tasks) in src/app/services.py
- [X] T009 Create basic input validation helper functions (e.g., for title length, ID parsing) in src/app/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with validation and unique IDs.

**Independent Test**: Add a task via the console and then verify its existence and details by viewing tasks (after View Tasks is implemented).

### Implementation for User Story 1

- [X] T010 [US1] Generate `add_task()` function in src/app/services.py to handle task creation, ID assignment, and input validation.
- [X] T011 [US1] Generate console menu option for "Add Task" in src/app/main.py.
- [X] T012 [US1] Generate user input handling for "Add Task" in src/app/main.py, integrating with services.py and utils.py.

---

## Phase 4: User Story 2 - View Tasks (Priority: P1)

**Goal**: Allow users to display a list of all existing tasks.

**Independent Test**: View tasks via the console and verify that all tasks (added by User Story 1) are displayed correctly, or a "No tasks found" message is shown if the list is empty.

### Implementation for User Story 2

- [X] T013 [US2] Generate `get_tasks()` function in src/app/services.py to retrieve all stored tasks.
- [X] T014 [US2] Generate console menu option for "View Tasks" in src/app/main.py.
- [X] T015 [US2] Generate task display logic in src/app/main.py to format and show tasks, including "No tasks found" message.

---

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: Provide functionality to modify existing task details by ID.

**Independent Test**: Add a task, then update its title/description, and verify the change by viewing tasks. Test handling of non-existent IDs.

### Implementation for User Story 3

- [X] T016 [US3] Generate `update_task()` function in src/app/services.py to update task details by ID, including validation and error handling for non-existent IDs.
- [X] T017 [US3] Generate console menu option for "Update Task" in src/app/main.py.
- [X] T018 [US3] Generate user input handling for "Update Task" in src/app/main.py, including handling non-existent IDs.

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to remove tasks by ID with a confirmation step.

**Independent Test**: Add a task, delete it (with confirmation), and verify its removal by viewing tasks. Test handling of non-existent IDs.

### Implementation for User Story 4

- [X] T019 [US4] Generate `delete_task()` function in src/app/services.py to remove a task by ID, including confirmation logic and error handling for non-existent IDs.
- [X] T020 [US4] Generate console menu option for "Delete Task" in src/app/main.py.
- [X] T021 [US4] Generate user input handling for "Delete Task" in src/app/main.py, including handling non-existent IDs and confirmation.

---

## Phase 7: User Story 5 - Mark as Complete / Incomplete (Priority: P2)

**Goal**: Enable users to toggle the completion status of a task by ID.

**Independent Test**: Add a task, mark it complete, view its status, then mark it incomplete, and view its status again. Test handling of non-existent IDs.

### Implementation for User Story 5

- [X] T022 [US5] Generate `toggle_complete()` function in src/app/services.py to change the completion status of a task by ID.
- [X] T023 [US5] Generate console menu option for "Mark Complete/Incomplete" in src/app/main.py.
- [X] T024 [US5] Generate user input handling for "Mark Complete/Incomplete" in src/app/main.py, including handling non-existent IDs.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final application improvements and cleanup.

- [X] T025 Generate the main application loop and menu in src/app/main.py, ensuring graceful exit and robust handling of invalid menu choices.
- [X] T026 Update README.md with comprehensive setup and run instructions based on quickstart.md.
- [X] T027 Refine error handling and user feedback mechanisms across src/app/services.py and src/app/main.py.
- [X] T028 Ensure all AI-generated code adheres to Python best practices for style, readability, and maintainability.

---

## Phase 9: Testing

**Purpose**: Comprehensive manual testing of the implemented features.

-   [ ] T029 Manually test the "Add -> View -> Update -> View" flow using the `quickstart.md` instructions.
-   [ ] T030 Manually test the "Delete -> confirm empty state" flow using the `quickstart.md` instructions.
-   [ ] T031 Manually test "Toggle completion repeatedly" for a task using the `quickstart.md` instructions.
-   [ ] T032 Manually test invalid inputs (e.g., empty title, too long title, non-existent ID, non-numeric ID, wrong menu choice) for all operations.
-   [ ] T033 Verify that the program does not crash under any valid or invalid input scenario.
-   [ ] T034 Verify that the console application loops continuously, allowing repeated operations without requiring a restart.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately.
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
-   **User Stories (Phase 3-7)**: All depend on Foundational phase completion. User Stories can then proceed with some parallelism, or sequentially in priority order (P1, P2).
-   **Polish & Cross-Cutting Concerns (Phase 8)**: Depends on all user stories (Phase 3-7) being largely complete.
-   **Testing (Phase 9)**: Depends on Polish & Cross-Cutting Concerns (Phase 8) being complete.

### User Story Dependencies

-   **User Story 1 (Add Task - P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   **User Story 2 (View Tasks - P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
-   **User Story 3 (Update Task - P2)**: Logically depends on User Story 1 (Add Task) to create data and User Story 2 (View Tasks) for verification.
-   **User Story 4 (Delete Task - P2)**: Logically depends on User Story 1 (Add Task) to create data and User Story 2 (View Tasks) for verification.
-   **User Story 5 (Mark as Complete / Incomplete - P2)**: Logically depends on User Story 1 (Add Task) to create data and User Story 2 (View Tasks) for verification.

### Within Each User Story

-   Model definition (src/app/models.py) precedes service logic (src/app/services.py).
-   Service logic (src/app/services.py) precedes CLI/UI integration (src/app/main.py).
-   Core implementation for a feature precedes its integration into the main menu loop.

### Parallel Opportunities

-   All Setup tasks (T001-T006) can run in parallel, as they involve creating directories and empty files.
-   Once the Foundational phase (Phase 2) is complete, User Story 1 (Add Task) and User Story 2 (View Tasks) can be developed with some parallelism, as their core service functions are distinct.
-   The implementation tasks within a user story can be parallelized if they operate on different files (e.g., generating service logic and then menu option in `main.py`).
-   The console menu options for different CRUD operations (e.g., T011, T014, T017, T020, T023) can be developed in parallel once their underlying service functions are available.
-   The manual Testing tasks (T029-T034) are largely independent and can be executed in parallel for different scenarios once the core implementation is complete.

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1.  Complete Phase 1: Setup (T001-T006)
2.  Complete Phase 2: Foundational (T007-T009)
3.  Complete Phase 3: User Story 1 (Add Task - T010-T012)
4.  Complete Phase 4: User Story 2 (View Tasks - T013-T015)
5.  **STOP and VALIDATE**: Test "Add Task" and "View Tasks" independently. This forms the minimal viable product.

### Incremental Delivery

1.  Complete Setup + Foundational -> Foundation ready.
2.  Implement User Story 1 (Add Task) -> Test independently -> Demo.
3.  Implement User Story 2 (View Tasks) -> Test independently -> Demo.
4.  Implement User Story 3 (Update Task) -> Test independently -> Demo.
5.  Continue with User Story 4, then User Story 5.
6.  Each story adds value without breaking previous stories.

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together.
2.  Once Foundational is done:
    *   Developer A: Focus on User Story 1 (Add Task) and User Story 2 (View Tasks).
    *   Developer B: Focus on User Story 3 (Update Task) and User Story 4 (Delete Task).
    *   Developer C: Focus on User Story 5 (Mark Complete/Incomplete) and later Polish & Testing.
3.  Stories complete and integrate independently.

---

## Notes

-   [P] tasks = different files, no dependencies.
-   [Story] label maps task to specific user story for traceability.
-   Each user story should be independently completable and testable.
-   Commit after each task or logical group.
-   Stop at any checkpoint to validate story independently.
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence.
