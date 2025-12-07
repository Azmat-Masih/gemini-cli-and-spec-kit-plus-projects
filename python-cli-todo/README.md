# Phase I: In-Memory Python Console Todo Application

This project implements Phase I of the multi-phase Todo Application, focusing on a fully functional, in-memory Python console application. It demonstrates basic CRUD (Create, Read, Update, Delete) functionality for todo items, adhering to Spec-Driven Development (SDD) principles.

## Features

*   **Add Task**: Create a new todo item with a title and optional description.
*   **View Tasks**: Display a list of all tasks with their ID, title, and completion status.
*   **Update Task**: Modify the title and/or description of an existing task.
*   **Delete Task**: Remove a task by its ID with user confirmation.
*   **Mark as Complete/Incomplete**: Toggle the completion status of a task.

## Getting Started

### Prerequisites

*   **Python 3.13+**: Ensure you have a compatible Python version installed.
*   **UV**: A modern Python package manager. If you don't have UV, you can install it using pip:
    ```bash
    pip install uv
    ```

### Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/hackathon_2_cli_todo_phase_1.git # Replace with your repository URL
    cd hackathon_2_cli_todo_phase_1
    ```

2.  **Create a virtual environment and install dependencies** using UV:
    ```bash
    uv venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```
    *Note: Phase I has no external dependencies beyond the standard Python library.*

## Running the Application

1.  **Activate your virtual environment**:
    ```bash
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    ```

2.  **Run the main application**:
    ```bash
    python src/app/main.py
    ```

## Interacting with the Application

The application provides a text-based menu. Follow the on-screen prompts to perform various operations:
*   Enter `1` to Add a new task.
*   Enter `2` to View all tasks.
*   Enter `3` to Update an existing task.
*   Enter `4` to Delete a task.
*   Enter `5` to Toggle the completion status of a task.
*   Enter `0` to Exit the application.

---
**Important Note**: This is an **in-memory application**. All tasks created or modified will be lost when the application is closed. This is by design for Phase I.

## Project Structure

```
.
├── .gemini/                 # Gemini CLI configuration
├── .specify/                # Spec-Kit Plus templates and scripts
├── history/                 # Prompt History Records
├── specs/                   # Feature specifications and planning documents
│   └── 001-phase1-console-todo/
│       ├── spec.md          # Feature Specification
│       ├── plan.md          # Implementation Plan
│       ├── data-model.md    # Data Model Definition
│       ├── quickstart.md    # Quickstart Guide
│       ├── tasks.md         # Detailed Task List
│       └── checklists/
│           └── requirements.md # Spec Quality Checklist
└── src/
    └── app/
        ├── main.py          # Main console UI and application logic
        ├── models.py        # Task data model definition
        ├── services.py      # Core task management (CRUD) logic
        └── utils.py         # Utility functions (input handling, printing)
```
