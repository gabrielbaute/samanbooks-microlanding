from pydantic import BaseModel
from datetime import datetime

class DownloadsCreate(BaseModel):
    """Schemas for downloads"""
    date: datetime
    filename: str

class DownloadsResponse(DownloadsCreate):
    """Schemas for downloads response"""
    id: int
    date: datetime
    filename: str

    class Config:
        from_attributes = True