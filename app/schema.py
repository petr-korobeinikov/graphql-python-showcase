import graphene

from app import storage


class Person(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()


class Task(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)
    person = graphene.Field(Person, name='assignee')

    async def resolve_person(parent, info):
        assignee_id = storage.task_by_id(parent.id).first().assignee
        person = storage.person_by_id(assignee_id).first()

        return Person(id=person.id, name=person.name)


class Project(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    slug = graphene.String(required=True)
    tasks = graphene.List(Task)

    async def resolve_tasks(parent, info):
        return [Task(id=task.id, title=task.title) for task in storage.tasks_by_project_id(parent.id)]


class Query(graphene.ObjectType):
    projects = graphene.List(Project)
    project_by_slug = graphene.Field(Project, slug=graphene.String(required=True))

    async def resolve_projects(parent, info):
        return storage.all_projects()

    async def resolve_project_by_slug(parent, info, slug):
        return storage.project_by_slug(slug).first()


schema = graphene.Schema(query=Query)
