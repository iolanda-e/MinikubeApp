import json
from pathlib import Path
from typing import List
from app.models.transaction_model import Transaction



DATA_FILE = Path("data/transactions.json")


def get_transactions() -> List[Transaction]:
    """Load all transactions from the JSON file."""
    raw = DATA_FILE.read_text(encoding="utf-8")
    items = json.loads(raw)  # listă de dict-uri

    return [Transaction.model_validate(item) for item in items]
