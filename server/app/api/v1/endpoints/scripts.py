from fastapi import APIRouter
router = APIRouter()
@router.get("/")
async def get_scripts(): return []
@router.post("/")
async def create_script(): return {"id": "123"}
