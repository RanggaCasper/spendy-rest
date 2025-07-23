from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Transaction(BaseModel):
    name: str
    notes: Optional[str] = None
    amount: float
    type: str
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
