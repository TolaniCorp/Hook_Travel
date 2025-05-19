# formatter.py
# Utility functions for formatting currency, dates, and user-friendly labels

from datetime import datetime

def format_currency(amount: float, currency: str = "USD") -> str:
    return f"{currency} {amount:,.2f}"

def format_date(date_str: str) -> str:
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%B %d, %Y")
    except ValueError:
        return date_str

def safe_join(items, sep=', '):
    return sep.join(filter(None, items))
