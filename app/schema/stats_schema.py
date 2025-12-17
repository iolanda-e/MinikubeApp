from datetime import date
from pydantic import BaseModel
from typing import Dict, Optional


class SummaryStats(BaseModel):
    """Schema representing summary statistics for expenses."""
    from_date: date
    to_date: date
    currency: str
    total_expenses: float
    transactions_count: int
    average_expense: float | None = None
    max_expense: float | None = None

class CategoryStats(BaseModel):
    """Schema representing category-wise statistics for expenses."""
    from_date: date
    to_date: date
    currency: str = "RON"
    category: Optional[str] = None
    total_expenses: Optional[float] = None

