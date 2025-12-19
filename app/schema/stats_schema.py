from datetime import date
from pydantic import BaseModel
from typing import Dict, List, Optional


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


class TopCategoryItem(BaseModel):
    """Schema representing a single top category item."""
    category: str
    total_expenses: float
    percentage: float


class TopCategoriesStats(BaseModel):
    """Schema representing top categories statistics for expenses."""
    from_date: date
    to_date: date
    currency: str = "RON"
    limit: int
    total_expenses: float
    items: List[TopCategoryItem]