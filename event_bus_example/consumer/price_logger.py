import logging

from event_bus_example.event import PriceTick

logger = logging.getLogger(__name__)


class PriceLogger:

    def log(self, pt: PriceTick):
        logger.info(str(pt))
