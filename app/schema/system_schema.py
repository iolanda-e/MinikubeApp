from datetime import date
from typing import List, Optional

from pydantic import BaseModel


class ServiceInfo(BaseModel):
    """Schema representing basic information about the service."""
    service: str
    version: str
    log_level: str
    currency: str
    total_transactions: int
    date_from: Optional[date] = None
    date_to: Optional[date] = None
    available_stats: List[str]
