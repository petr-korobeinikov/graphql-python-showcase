import uvicorn

from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from starlette.routing import Route

from app.schema import schema

routes = [
    Route('/', GraphQLApp(
        schema=schema,
        executor_class=AsyncioExecutor
    ))
]

app = Starlette(routes=routes)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
