class Task:
    _next_id = 1

    def __init__(self, title: str, description: str = None, completed: bool = False):
        if not isinstance(title, str) or not (1 <= len(title) <= 200):
            raise ValueError("Title must be a string between 1 and 200 characters.")
        if description is not None and (not isinstance(description, str) or len(description) > 1000):
            raise ValueError("Description must be a string and no longer than 1000 characters if provided.")
        if not isinstance(completed, bool):
            raise ValueError("Completed status must be a boolean.")

        self.id = Task._next_id
        Task._next_id += 1
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}: {self.title}" + (f" ({self.description})" if self.description else "")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }

    @staticmethod
    def reset_id():
        """Resets the ID counter for testing or fresh starts."""
        Task._next_id = 1
