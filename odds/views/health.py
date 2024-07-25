from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import Response

__all__ = ["router"]

router = APIRouter()


@router.get("/", name="health", response_description="Health check")
async def get_health_check(_: Request) -> Response:
    return Response("OK")
