from pydantic import BaseModel
from datetime import datetime

class DownloadsCreate(BaseModel):
    """Schemas for downloads"""
    date: datetime
    filename: str

    def to_dict(self) -> dict:
        return {
            'date': self.date,
            'filename': self.filename
        }

class DownloadsResponse(DownloadsCreate):
    """Schemas for downloads response"""
    id: int
    date: datetime
    filename: str

    class Config:
        from_attributes = True