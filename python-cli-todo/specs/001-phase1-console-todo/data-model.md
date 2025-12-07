# Data Model: Phase I In-Memory Python Console Todo Application

## Entity: Task

Represents a single todo item within the in-memory application.

### Fields:

*   **`id`**:
    *   **Type**: Integer
    *   **Description**: Unique identifier for the task.
    *   **Validation**: Auto-incremented, non-negative.
*   **`title`**:
    *   **Type**: String
    *   **Description**: The main title or name of the todo item.
    *   **Validation**: Required, minimum 1 character, maximum 200 characters.
*   **`description`**:
    *   **Type**: String
    *   **Description**: Optional longer description for the todo item.
    *   **Validation**: Optional, maximum 1000 characters.
*   **`completed`**:
    *   **Type**: Boolean
    *   **Description**: Indicates whether the task has been completed.
    *   **Validation**: Default value is `False`.

### Relationships:

*   None (stand-alone entity for in-memory storage)

### State Transitions:

*   A task's `completed` status can toggle between `True` and `False`.
