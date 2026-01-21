from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class ScriptBase(BaseModel):
    title: str
    content: str
    project_id: int
    persona_id: Optional[str] = None

class ScriptCreate(ScriptBase):
    pass

class ScriptUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None

class ScriptInDB(ScriptBase):
    id: str # MongoDB ID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
