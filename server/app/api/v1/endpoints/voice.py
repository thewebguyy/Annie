from fastapi import APIRouter, Body
from ....services.voice_service import voice_service

router = APIRouter()

@router.post("/clone")
async def clone_voice(persona_id: str, texts: list[str] = Body(...)):
    return voice_service.create_persona(persona_id, texts)

@router.post("/audit")
async def audit_brand(script_text: str = Body(...), persona_id: str = Body(...)):
    return voice_service.audit_script(script_text, persona_id)
