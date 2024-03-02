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
                 assigned_personnel: Optional[List[str]] = None,
                 comments: Optional[str] = ""
                 ) -> object:

        self.name = name
        self.assigner = assigner
        self.company = company
        self.deadline = deadline
        self._status = 'In progress'
        self.priority = priority if priority in [1, 2, 3] else 0
        self.description = description
        self.assigned_personnel = assigned_personnel
        self._creation_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self._last_modified_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.comments = comments

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status='Completed'):
        self._status = new_status

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def last_modified_date(self):
        return self._last_modified_date

    def _update_last_modified_date(self):
        self._last_modified_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def add_comment(self, new_comment):
        self.comments += f"\n {new_comment}"
        self._update_last_modified_date()

    def is_overdue(self):
        if self.deadline < datetime.now():
            return f"Task is overdue!"
        else:
            remaining_time = self.deadline - datetime.now()
            return f"You still have {remaining_time.days} days to do the task!"

    def __repr__(self):
        comments_str = ', '.join([f"'{comment}'" for comment in self.comments])

        return (f"{self.__class__.__name__}('{self.name}', '{self.assigner}', '{self.company}', "
                f"{self.priority}, '{self.description}', '{self.status}', {self.assigned_personnel}, "
                f"'{self.creation_date}', '{self.last_modified_date}', [{comments_str}])")
