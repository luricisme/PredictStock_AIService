from datetime import date, timedelta

def get_today() -> date:
    return date.today()

def get_days_before_today(days: int) -> date:
    if days < 0:
        raise ValueError("days must be >= 0")
    return date.today() - timedelta(days=days)