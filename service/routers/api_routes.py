from fastapi import APIRouter
from routers.routes import ping

from routes.auth import auth

from routes.users import users
from routes.users.count import count
from routes.users.me import me
from routes.users.register import register
from routes.users.login import login

from routes.computers import computers



def create_api_router() -> APIRouter:
    api_router = APIRouter()
    api_router.include_router(auth.router, tags=["auth"])
    api_router.include_router(users.router, tags=["users"])
    api_router.include_router(count.router, tags=["users"])
    api_router.include_router(me.router, tags=["users"])
    api_router.include_router(register.router, tags=["users"])
    api_router.include_router(login.router, tags=["users"])
    api_router.include_router(computers.router, tags=["computers"])
    api_router.include_router(ping.router, tags=["default"])
    return api_router


router = create_api_router()
