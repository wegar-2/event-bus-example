import logging

from event_bus_example.event import PriceTickEvent

logger = logging.getLogger(__name__)


class LogPriceSubscriber:

    def log(self, pt: PriceTickEvent):
        logger.info(str(pt))
