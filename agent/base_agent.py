# base_agent.py
import random

class BaseAgent:
    def __init__(self, name="Sizerra"):
        self.name = name
        self.tasks = []
        self.status = "idle"
    
    def add_task(self, task):
        """Add task to agent's task list."""
        self.tasks.append(task)
        self.status = "busy"
        print(f"{self.name} has added a new task: {task}")

    def perform_task(self):
        """Perform the task by randomly choosing one."""
        if self.tasks:
            task = self.tasks.pop(0)
            print(f"{self.name} is performing task: {task}")
            # Simulate task completion
            self.status = "idle"
            return f"{self.name} completed the task: {task}"
        else:
            print(f"{self.name} has no tasks to perform.")
            self.status = "idle"
            return f"{self.name} is idle."
    
    def get_status(self):
        """Returns the current status of the agent."""
        return self.status
