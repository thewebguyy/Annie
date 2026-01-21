from fastapi import APIRouter
from .endpoints import auth, scripts, retention, voice, hooks, research, reframe

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(scripts.router, prefix="/scripts", tags=["scripts"])
api_router.include_router(retention.router, prefix="/retention", tags=["retention"])
api_router.include_router(voice.router, prefix="/voice", tags=["voice"])
api_router.include_router(hooks.router, prefix="/hooks", tags=["hooks"])
api_router.include_router(research.router, prefix="/research", tags=["research"])
api_router.include_router(reframe.router, prefix="/reframe", tags=["reframe"])
