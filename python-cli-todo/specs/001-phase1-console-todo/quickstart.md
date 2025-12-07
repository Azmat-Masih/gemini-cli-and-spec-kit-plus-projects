# Quickstart Guide: Phase I In-Memory Python Console Todo Application

This guide will help you get the Phase I In-Memory Python Console Todo Application up and running quickly.

## Prerequisites

*   **Python 3.13+**: Ensure you have a compatible Python version installed.
*   **UV**: A modern Python package manager.

## Setup

1.  **Clone the repository** (if not already done):
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Navigate to the project root**:
    ```bash
    cd /mnt/d/Projects/hackathon_2_cli_todo_phase_1 # Adjust if your path is different
    ```

3.  **Create a virtual environment and install dependencies** using UV:
    ```bash
    uv venv
    source .venv/bin/activate # On Windows: .venv\Scripts\activate
    # No additional dependencies for Phase I
    ```

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

The application provides a text-based menu. Follow the on-screen prompts to:
*   Add new tasks
*   View existing tasks
*   Update tasks
*   Delete tasks
*   Mark tasks as complete or incomplete

---
**Note**: This is an in-memory application. All tasks will be lost when the application is closed.
