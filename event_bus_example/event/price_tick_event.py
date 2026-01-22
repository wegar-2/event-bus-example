from datetime import datetime

from pydantic import BaseModel

from event_bus_example.common import DATETIME_FORMAT


class PriceTickEvent(BaseModel):
    ticker: str
    price: float
    timestamp: datetime

    def __str__(self) -> str:
        return (f"Stock {self.ticker} price "
                f"at {self.timestamp.strftime(DATETIME_FORMAT)} is "
                f"{self.price:_.06f}")
