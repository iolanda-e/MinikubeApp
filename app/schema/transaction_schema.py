from datetime import date
from typing import Optional

from pydantic import BaseModel


class Transaction(BaseModel):
    """Schema representing a financial transaction."""
    id: int
    date: date             
    amount: float           
    currency: str = "RON"
    category: str
    merchant: Optional[str] = None
    description: Optional[str] = None
