from datetime import datetime


class Task:
    def __init__(self,
                 name: str,
                 assigner: str,
                 company: str,
                 deadline: time,
                 priority: int = 0,
                 description: str = "",
                 status: str = "Not started",
                 assigned_personnel: list = None,
                 creation_date: datetime = None,
                 last_modified_date: datetime = None,
                 comments: str = ""
                 ):

        self.name = name
        self.assigner = assigner
        self.company = company
        self.deadline = deadline
        self.priority = priority or [1, 2, 3]
        self.description = description
        self.status = status
        self.assigned_personnel = assigned_personnel
        self.creation_date = creation_date or datetime.now()
        self.last_modified_date = last_modified_date or self.creation_date
        self.comments = comments

    # String representation
    def __str__(self):
        return f"{self.name} assigned to {self.assigned_personnel} with the priority {self.priority}"

    # Comparison methods
    def __eq__(self, other):
        return self.priority == other.priority

    def __lt__(self, other):
        return self.priority < other.priority

    def is_overdue(self):
        return self.deadline < datetime.now()

    def update_task(self, new_priority, new_status):
        self.priority = new_priority
        self.status = new_status
        self.last_modified_date = datetime.now()

    def add_comment(self, new_comment):
        self.comments += f"\n {new_comment}"
        self.last_modified_date = datetime.now()