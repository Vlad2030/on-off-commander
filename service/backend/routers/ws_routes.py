from fastapi import APIRouter
from routers.routes import ping

from routes.ws import server
from routes.ws import computers



def create_ws_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(server.router, tags=["ws", "server", "auth"])
    api_router.include_router(computers.router, tags=["ws", "computers"])

    return api_router


router = create_ws_router()
