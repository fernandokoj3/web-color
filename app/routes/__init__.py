from typing import Iterable

from fastapi import APIRouter, FastAPI


def register_routes(app: FastAPI, routers: Iterable[APIRouter]):
    for router in routers:
        app.include_router(router)


def routes_config(app: FastAPI):
    from app.routes.web.home.home_router import  router as home_router

    routers = (
        home_router,
    )
    register_routes(app, routers)
