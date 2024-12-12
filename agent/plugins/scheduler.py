# scheduler.py
import threading
import time

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay):
        """Add a task to the schedule."""
        print(f"Task scheduled to run in {delay} seconds.")
        timer = threading.Timer(delay, task)
        self.tasks.append(timer)
        timer.start()

    def cancel_all_tasks(self):
        """Cancel all scheduled tasks."""
        for task in self.tasks:
            task.cancel()
        self.tasks.clear()
        print("All tasks have been canceled.")
