from datetime import datetime
from functional import seq

from app.entities import Person, Project, Task


def all_projects() -> [Project]:
    return [
        Project(id=1, name='Project 1', slug='proj1'),
        Project(id=2, name='Project 2', slug='proj2'),
        Project(id=3, name='Project 3', slug='proj3'),
    ]


def all_tasks() -> [Task]:
    return [
        Task(id=1, project_id=1, assignee=1, created_at=datetime.now(), title='Make foo', description=''),
        Task(id=1, project_id=1, assignee=1, created_at=datetime.now(), title='Make faz', description=''),
        Task(id=1, project_id=1, assignee=2, created_at=datetime.now(), title='Make fam', description=''),

        Task(id=1, project_id=2, assignee=2, created_at=datetime.now(), title='Make boo', description=''),
        Task(id=1, project_id=2, assignee=3, created_at=datetime.now(), title='Make bar', description=''),
        Task(id=1, project_id=2, assignee=3, created_at=datetime.now(), title='Make baz', description=''),

        Task(id=1, project_id=3, assignee=1, created_at=datetime.now(), title='Make qoo', description=''),
        Task(id=1, project_id=3, assignee=2, created_at=datetime.now(), title='Make qar', description=''),
        Task(id=1, project_id=3, assignee=3, created_at=datetime.now(), title='Make qaz', description=''),
    ]


def all_people() -> [Person]:
    return [
        Person(id=1, name='Person 1'),
        Person(id=2, name='Person 2'),
        Person(id=3, name='Person 3'),
    ]


def project_by_slug(slug: str) -> [Project]:
    return seq(all_projects()).filter(lambda p: p.slug == slug)


def tasks_by_project_id(project_id: int) -> [Task]:
    return seq(all_tasks()).filter(lambda t: t.project_id == project_id)
