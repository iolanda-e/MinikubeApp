from datetime import date
from typing import List

from fastapi import APIRouter, Query, HTTPException

from app.controllers.helpers import filter_by_date
from app.data.loader import get_transactions
from app.schema.transaction_schema import Transaction 
from app.schema.stats_schema import TopCategoriesStats, TopCategoryItem

router = APIRouter()

@router.get(
    "/top-categories",
    response_model=TopCategoriesStats,
    summary="Get top spending categories",
    response_description="Top N categories by total expenses for the given date range.",
    tags=["Stats"],
)
def get_top_categories(
    from_date: date = Query(..., alias="from"),
    to_date: date = Query(..., alias="to"),
    limit: int = Query(3, ge=1, le=20, description="Max number of top categories to return"),
):
    """
    Returns the top N categories by total expenses in the given date range.
    """
    transactions: List[Transaction] = get_transactions()
    filtered = filter_by_date(transactions, from_date, to_date)

    if not filtered:
        raise HTTPException(
            status_code=404,
            detail="No expenses found in the given date range.",
        )

    category_totals: dict[str, float] = {}
    for tx in filtered:
        category_totals[tx.category] = category_totals.get(tx.category, 0.0) + tx.amount

    total_expenses = sum(category_totals.values())

    sorted_items = sorted(
        category_totals.items(),
        key=lambda kv: kv[1],
        reverse=True,
    )[:limit]

    items: List[TopCategoryItem] = []
    for cat, total in sorted_items:
        percentage = round((total / total_expenses) * 100, 2) if total_expenses > 0 else 0.0
        items.append(
            TopCategoryItem(
                category=cat,
                total_expenses=total,
                percentage=percentage,
            )
        )

    return TopCategoriesStats(
        from_date=from_date,
        to_date=to_date,
        currency="RON",
        limit=limit,
        total_expenses=total_expenses,
        items=items,
    )
