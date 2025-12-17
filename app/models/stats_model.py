from datetime import date
from pydantic import BaseModel


class SummaryStats(BaseModel):
    """Model representing summary statistics for expenses."""
    from_date: date
    to_date: date
    currency: str
    total_expenses: float
    transactions_count: int
    average_expense: float | None = None
    max_expense: float | None = None
