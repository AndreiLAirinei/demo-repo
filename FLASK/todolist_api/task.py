from datetime import datetime
from typing import List, Optional


class Task:

    def __init__(self,
                 name: str,
                 assigner: str,
                 company: str,
                 deadline: Optional[datetime] = None,
                 priority: Optional[int] = 0,
                 description: Optional[str] = "",
                 status: str = "Not started",
                 assigned_personnel: Optional[List[str]] = None,
                 creation_date: Optional[datetime] = None,
                 last_modified_date: Optional[datetime] = None,
                 comments: Optional[str] = ""
                 ):

        self.name = name
        self.assigner = assigner
        self.company = company
        self.deadline = deadline
        self.priority = priority if priority in [1, 2, 3] else 0
        self.description = description
        self.status = status
        self.assigned_personnel = assigned_personnel
        self.creation_date = creation_date if creation_date else datetime.now()
        self.last_modified_date = last_modified_date if last_modified_date else self.creation_date
        self.comments = comments

    # Comparison methods
    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def is_overdue(self):
        if self.deadline < datetime.now():
            return f"Task is overdue!"
        elif self.deadline >= datetime.now():
            remaining_time = self.deadline - datetime.now()
            return f"You still have {remaining_time.days} days to do the task!"

    def update_task(self, new_priority, new_status):
        self.priority = new_priority
        self.status = new_status
        self.last_modified_date = datetime.now()

    def add_comment(self, new_comment):
        self.comments += f"\n {new_comment}"
        self.last_modified_date = datetime.now()

    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.name}', '{self.assigner}', '{self.company}', "
                f"{self.priority}, '{self.description}', '{self.status}', {self.assigned_personnel}, "
                f"'{self.creation_date}', '{self.last_modified_date}', '{self.comments}')")


# if __name__ == "__main__":
#
#     task_instance = Task(
#         task_id="task1",
#         name="Example Task",
#         assigner="John Doe",
#         company="ABC Inc",
#         deadline=datetime(2025, 12, 4),
#         priority=2,
#         description="A random description",
#         status="In Progress",
#         assigned_personnel=["Alice", "Bob"],
#         creation_date=datetime(2024, 2, 1),
#         last_modified_date=datetime(2024, 2, 15),
#         comments="Some comments"
#     )
#
#     print(repr(task_instance))
#     print(Task.is_overdue(task_instance))
