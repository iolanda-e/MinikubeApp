from typing import List

from fastapi import APIRouter

from app.data.loader import get_transactions
from app.schema.transaction_schema import Transaction
from app.schema.system_schema import ServiceInfo
from app.config import SERVICE_NAME, SERVICE_VERSION, LOG_LEVEL, CURRENCY

router = APIRouter()


@router.get(
    "/health",
    tags=["System"],
    summary="Health check endpoint",
    response_description="Simple liveness check for the service.",
)
def health():
    return {"status": "ok"}


@router.get(
    "/info",
    response_model=ServiceInfo,
    tags=["System"],
    summary="Service information",
    response_description="Basic information about the Expense Stats service.",
)
def get_info():
    transactions: List[Transaction] = get_transactions()
    total = len(transactions)

    if total > 0:
        dates = sorted(tx.date for tx in transactions)
        date_from = dates[0]
        date_to = dates[-1]
    else:
        date_from = None
        date_to = None

    return ServiceInfo(
        service=SERVICE_NAME,
        version=SERVICE_VERSION,
        log_level=LOG_LEVEL,
        currency=CURRENCY,
        total_transactions=total,
        date_from=date_from,
        date_to=date_to,
        available_stats=[
            "/stats/summary",
            "/stats/by-category",
            "/stats/top-categories",
            "/stats/daily",
        ],
    )
