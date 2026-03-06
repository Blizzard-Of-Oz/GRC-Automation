"""FastAPI application entrypoint."""

from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings


def create_app() -> FastAPI:
    """Create and configure FastAPI app instance."""
    application = FastAPI(
        title=settings.app_name,
        debug=settings.app_debug,
        version="0.1.0",
    )
    application.include_router(health_router, prefix="/api/v1")
    return application


app = create_app()
