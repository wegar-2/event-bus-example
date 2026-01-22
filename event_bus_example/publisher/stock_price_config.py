from pydantic import BaseModel


class StockPriceConfig(BaseModel):
    ticker: str = "ABCDE"
    price: float = 100
    mu_daily: float = 0.01
    sigma_daily: float = 0.02
    seed: int = 123_456
