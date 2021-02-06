import graphene
import uvicorn

from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    async def resolve_hello(self, info, name):
        return "Hello " + name


routes = [
    Route('/', GraphQLApp(
        schema=graphene.Schema(query=Query),
        executor_class=AsyncioExecutor
    ))
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
