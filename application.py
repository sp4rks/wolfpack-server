import os

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from v1.app import routes as v1_routes


async def base(request):
    return JSONResponse({
        'name': 'Wolfpack Squad Server'
    })

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

routes = [
    Route('/', endpoint=base),
    Mount('/v1', routes=v1_routes)
]

application = Starlette(routes=routes, middleware=middleware)

if __name__ == '__main__':
    uvicorn.run(
        'application:application',
        host='0.0.0.0',
        port=8000,
        reload=os.environ['RELOAD']
    )
