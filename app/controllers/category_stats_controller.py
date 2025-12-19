from datetime import date
from typing import List

from fastapi import APIRouter, Query, HTTPException
from app.controllers.helpers import filter_by_date
from app.data.loader import get_transactions
from app.schema.transaction_schema import Transaction  
from app.schema.stats_schema import CategoryStats  

router = APIRouter()

@router.get(
    "/by-category",
    response_model=CategoryStats,
    summary="Get expenses by category",
    response_description="Expense totals aggregated by category or for a single category.",
    tags=["Stats"]
)
def get_expenses_by_category(
    from_date: date = Query(..., alias="from"),
    to_date: date = Query(..., alias="to"),
    category: str = Query(..., description="Category to filter by"),
    tags=["Stats"]
):
    """
    Returns expenses grouped by category for the given date range.
    """
    transactions: List[Transaction] = get_transactions()
    filtered = filter_by_date(transactions, from_date, to_date)
    cat_tx = [tx for tx in filtered if tx.category == category]

    if not cat_tx:
        raise HTTPException(
            status_code=404,
            detail=f"No expenses found for category '{category}' in given date range."
        )
    
    total = sum(tx.amount for tx in cat_tx)
    
    return CategoryStats(
        from_date=from_date,
        to_date=to_date,
        currency="RON",
        category=category,
        total_expenses=total,
    )

