"""Healthcheck endpoint definitions."""

from fastapi import APIRouter
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """API health payload."""

    status: str
    service: str


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def healthcheck() -> HealthResponse:
    """Simple liveness endpoint."""
    return HealthResponse(status="ok", service="grc-automation-platform")
