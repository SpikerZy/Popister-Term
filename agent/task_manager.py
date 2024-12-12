# task_manager.py
from agent.base_agent import BaseAgent
import random

class TaskManager(BaseAgent):
    def __init__(self, name="TaskManager"):
        super().__init__(name)
    
    def assign_random_task(self):
        """Assign a random task to the agent."""
        task_list = [
            "Analyze data",
            "Check blockchain status",
            "Review AI training models",
            "Collect user feedback"
        ]
        task = random.choice(task_list)
        self.add_task(task)
        print(f"Task Manager assigned: {task}")
    
    def process_tasks(self):
        """Processes all tasks for the agent."""
        while self.tasks:
            task_result = self.perform_task()
            print(task_result)
