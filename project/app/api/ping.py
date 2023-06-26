from fastapi import APIRouter, Depends

from app.config import get_settings, Settings
from app.models.pydantic import PongResponseSchema

router = APIRouter()


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)) -> PongResponseSchema:
    return PongResponseSchema(
        ping="pong!",
        environment=settings.environment,
        testing=settings.testing
    )
