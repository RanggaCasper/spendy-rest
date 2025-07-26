from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    name: str
    notes: Optional[str] = None
    amount: float
    type: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
