from fastapi import APIRouter
from ....services.research_service import research_service

router = APIRouter()

@router.get("/query")
async def research_query(q: str):
    return research_service.query_facts(q)
