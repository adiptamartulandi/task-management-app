from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/_health")
async def health(request: Request):
    return JSONResponse(dict(status="OK"), status_code=200)
