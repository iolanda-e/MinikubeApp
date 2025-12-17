from datetime import date
from typing import List

from fastapi import APIRouter, Query, HTTPException

from app.data.loader import get_transactions
from app.schema.transaction_schema import Transaction
from app.schema.stats_schema import SummaryStats

router = APIRouter()


@router.get("/summary",
             response_model=SummaryStats,
             summary="Get expense summary statistics",
             response_description="Summary statistics for the selected date range",)
def get_summary(
    from_date: date = Query(..., alias="from"),
    to_date: date = Query(..., alias="to"),
):
    """
    Return summary statistics for all expenses between from_date and to_date (inclusive).
    """
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="'from' must be <= 'to'")

    transactions: List[Transaction] = get_transactions()

    filtered = [
        tx for tx in transactions
        if from_date <= tx.date <= to_date
    ]

    total = sum(tx.amount for tx in filtered)
    count = len(filtered)
    avg = total / count if count > 0 else None
    max_expense = max((tx.amount for tx in filtered), default=None)

    return SummaryStats(
        from_date=from_date,
        to_date=to_date,
        currency="RON",
        total_expenses=total,
        transactions_count=count,
        average_expense=avg,
        max_expense=max_expense,
    )
