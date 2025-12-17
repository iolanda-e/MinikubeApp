from datetime import date
from typing import List
from fastapi import HTTPException
from app.schema.transaction_schema import Transaction  

def filter_by_date(
    transactions: List[Transaction],
    from_date: date,
    to_date: date,
) -> List[Transaction]:
    """Return only transactions between from_date and to_date (inclusive)."""
    if from_date > to_date:
        raise HTTPException(status_code=400, detail="'from' must be <= 'to'")

    return [
        tx for tx in transactions
        if from_date <= tx.date <= to_date
    ]