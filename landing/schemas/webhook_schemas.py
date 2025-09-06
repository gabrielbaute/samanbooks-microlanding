from typing import Optional
from pydantic import BaseModel
from landing.enums import WebhookPriority

class WebhookPayload(BaseModel):
    event: str
    priority: WebhookPriority
    description: str
    tags: Optional[str]
    click: Optional[str]
    title: Optional[str]
    url: Optional[str]
    data: dict