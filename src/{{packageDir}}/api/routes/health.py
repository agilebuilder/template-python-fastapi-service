from fastapi import APIRouter

from ...core.config import settings

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok", "app": settings.app_name}
