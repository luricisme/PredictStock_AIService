from datetime import datetime
from app.schemas.candle import Candle

def map_raw_candle(c: dict) -> Candle:
    return Candle(
        time=datetime.utcfromtimestamp(c["time"] / 1000),
        open=c["open"],
        high=c["high"],
        low=c["low"],
        close=c["close"],
        volume=c["volume"]
    )