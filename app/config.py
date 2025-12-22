import os

SERVICE_NAME = "Expense Stats API"
SERVICE_VERSION = "1.0.0"
CURRENCY = "RON"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
