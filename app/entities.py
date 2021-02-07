from dataclasses import dataclass
from datetime import datetime


@dataclass
class Project:
    id: int
    name: str
    slug: str


@dataclass
class Task:
    id: int
    project_id: int
    assignee: int
    created_at: datetime
    title: str
    description: str


@dataclass
class Person:
    id: int
    name: str
