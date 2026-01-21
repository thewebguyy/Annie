from fastapi import APIRouter, Body
from ....services.reframer_service import reframer_service

router = APIRouter()

@router.post("/process")
async def reframe_content(script_text: str = Body(...), platforms: list[str] = Body(...)):
    result = await reframer_service.reframe_script(script_text, platforms)
    return result
