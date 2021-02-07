import graphene
import uvicorn

from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route


class Task(graphene.ObjectType):
    id = graphene.ID(required=True)
    title = graphene.String(required=True)


class Project(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    slug = graphene.String(required=True)
    tasks = graphene.List(Task)


class Query(graphene.ObjectType):
    projects = graphene.List(Project)
    project_by_slug = graphene.Field(Project, slug=graphene.String(required=True))

    async def resolve_projects(self, info):
        return [
            Project(id=1, name="Project 1", slug="proj1", tasks=[
                Task(id=1, title="Task 1"),
                Task(id=2, title="Task 1"),
                Task(id=3, title="Task 1"),
            ]),
            Project(id=2, name="Project 2", slug="proj2", tasks=[
                Task(id=4, title="Task 4"),
                Task(id=5, title="Task 5"),
                Task(id=6, title="Task 6"),
            ]),
            Project(id=3, name="Project 3", slug="proj3", tasks=[
                Task(id=7, title="Task 7"),
                Task(id=8, title="Task 8"),
                Task(id=9, title="Task 9"),
            ]),
        ]

    async def resolve_project_by_slug(self, info, slug):
        p = Project(id=3, name="Project 3", slug=slug, tasks=[
            Task(id=7, title="Task 7"),
            Task(id=8, title="Task 8"),
            Task(id=9, title="Task 9"),
        ])

        return p


routes = [
    Route('/', GraphQLApp(
        schema=graphene.Schema(query=Query),
        executor_class=AsyncioExecutor
    ))
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
