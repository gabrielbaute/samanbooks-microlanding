from pydantic import BaseModel
from datetime import datetime

class VisitsCreate(BaseModel):
    """Schema for visits creation"""
    date: datetime
    route: str

class VisitsResponse(BaseModel):
    """Schema for visits response"""
    id: int
    date: datetime
    route: str
    
    class Config:
        from_attributes = True