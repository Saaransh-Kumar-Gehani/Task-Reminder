import json
from datetime import datetime

class TaskManager:
    def __init__(self, storage_file="Files\\storage.json"):
        # This file will store tasks in JSON format
        self.storage_file = storage_file
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        # Try to read tasks from the JSON file
        try:
            with open(self.storage_file, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            # File doesn't exist yet → start with empty task list
            self.tasks = []

    def save_tasks(self):
        # Save current task list to JSON file
        with open(self.storage_file, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, description, time_str, reminder = True):
        task = {
            "description": description,
            "time": time_str,
            "done": False,
            "created": datetime.now().isoformat(),
            "reminder": reminder
        }
        self.tasks.append(task)
        self.save_tasks()

    def list_tasks(self):
        return [
            f"{i+1}. {'[x]' if t['done'] else '[ ]'} {t['description']} at {t['time']}"
            for i, t in enumerate(self.tasks)
        ]

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()
