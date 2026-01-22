from datetime import datetime
import logging
import math
import time
from typing import Final

import numpy as np

from event_bus_example.common import SECONDS_PER_DAY
from event_bus_example.event import PriceTickEvent
from event_bus_example.event_bus.event_bus import EventBus
from event_bus_example.publisher.config import StockPriceConfig

logger = logging.getLogger(__name__)


class StockPricePublisher:

    _PUBLISH_FREQ_IN_SECS: Final[int] = 3

    def __init__(self, bus: EventBus, config: StockPriceConfig):
        self._bus: EventBus = bus
        self._config: StockPriceConfig = config
        self._rng = np.random.default_rng(seed=self._config.seed)

    def stream(self):

        logger.info("Before start of stock price streaming...")
        price: float = self._config.price

        while True:

            time.sleep(3)

            price = price + (
                self._config.mu_daily *
                self._PUBLISH_FREQ_IN_SECS / SECONDS_PER_DAY
            ) + (
                math.sqrt(self._PUBLISH_FREQ_IN_SECS / SECONDS_PER_DAY) *
                float(self._rng.normal(size=1)[0]) *
                self._config.sigma_daily
            )

            logger.info(f"New price update available...")
            self._bus.publish(event=PriceTickEvent(
                ticker=self._config.ticker,
                price=price,
                timestamp=datetime.now()
            ))
