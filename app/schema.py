import graphene

from app import storage


class Task(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)


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
