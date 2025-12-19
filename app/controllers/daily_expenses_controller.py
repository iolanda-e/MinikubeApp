from app.schema.stats_schema import  DailyStats, DailyExpenseItem
from datetime import date
from typing import List
from fastapi import APIRouter, Query
from app.controllers.helpers import filter_by_date
from app.data.loader import get_transactions
from app.schema.transaction_schema import Transaction  

router = APIRouter()

@router.get(
    "/daily",
    response_model=DailyStats,
    summary="Get daily expenses over a date range",
    response_description="Total expenses per day within the given date range.",
    tags=["Stats"],
)
def get_daily_expenses(
    from_date: date = Query(..., alias="from"),
    to_date: date = Query(..., alias="to"),
):
    """
    Returns total expenses per day for the given date range.
    Only days that have at least one transaction are returned.
    """
    transactions: List[Transaction] = get_transactions()
    filtered = filter_by_date(transactions, from_date, to_date)

    daily_totals: dict[date, float] = {}
    for tx in filtered:
        daily_totals[tx.date] = daily_totals.get(tx.date, 0.0) + tx.amount

    items: List[DailyExpenseItem] = [
        DailyExpenseItem(date=day, total_expenses=total)
        for day, total in sorted(daily_totals.items(), key=lambda kv: kv[0])
    ]

    return DailyStats(
        from_date=from_date,
        to_date=to_date,
        currency="RON",
        items=items,
    )
