from fastapi import FastAPI

from app import bootstrap
from app.routes import routes_config


async def _fastapi_startup(fastapi: FastAPI):
    from app.config.error_handler import configure_exception_handlers

    await bootstrap.startup()

    routes_config(fastapi)

    configure_exception_handlers(fastapi)


async def _fastapi_shutdown(_: FastAPI):
    await bootstrap.shutdown()


# noinspection PyTypeChecker
def create_fastapi_application() -> FastAPI:
    from fastapi import FastAPI

    async def _startup():
        await _fastapi_startup(fastapi)

    async def _shutdown():
        await _fastapi_shutdown(fastapi)

    fastapi = FastAPI(
        title="Web color",
        version="1.0.0",
        on_startup=[_startup],
        on_shutdown=[_shutdown],
    )

    from app.config.error_handler import configure_exception_handlers

    configure_exception_handlers(fastapi)

    return fastapi


"""
For LOCAL development
"""
if __name__ == "__main__":
    # Start singles
    import uvicorn

    uvicorn.run(
        "app.main:create_fastapi_application",
        host="0.0.0.0",  # nosec
        port=5000,
        reload=True,
        log_level="info",
    )
