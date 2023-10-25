from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse
from schemas.responses.ping import PingResponse

router = APIRouter(prefix="/ping")

@router.get(
    path="/",
    response_model=PingResponse,
    status_code=status.HTTP_200_OK,
    summary="Server health check",
    description="Ping endpoint",
    response_description="If 'ok': true, then server is running successfully",
)
async def get_ping() -> ORJSONResponse:
    ping = PingResponse(ok=True)
    return ORJSONResponse(
        content=ping.dict(),
        status_code=status.HTTP_200_OK,
        )