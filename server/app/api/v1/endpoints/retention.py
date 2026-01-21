from fastapi import APIRouter, Body
from ....services.retention_service import retention_service

router = APIRouter()

@router.post("/analyze")
async def analyze_retention(script_text: str = Body(..., embed=True)):
    analysis = retention_service.analyze_pacing(script_text)
    chapters = retention_service.generate_chapters(script_text)
    return {
        "analysis": analysis,
        "chapters": chapters
    }
