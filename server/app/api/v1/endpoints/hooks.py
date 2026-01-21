from fastapi import APIRouter, Body
from ....services.hook_service import hook_service

router = APIRouter()

@router.post("/analyze")
async def analyze_hook(script_text: str = Body(..., embed=True)):
    return hook_service.analyze_hook(script_text)

@router.post("/generate")
async def generate_variants(base_hook: str = Body(...), platform: str = Body(...)):
    variants = await hook_service.generate_variants(base_hook, platform)
    return {"variants": variants}
