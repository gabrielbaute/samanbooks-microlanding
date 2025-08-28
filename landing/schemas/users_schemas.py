from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    """Schema for updating an existing user."""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password_hash: Optional[str] = None

class UserResponse(BaseModel):
    """Schema for returning a user."""
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
    class Config:
        from_attributes = True