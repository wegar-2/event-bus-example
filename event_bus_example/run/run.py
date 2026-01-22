from event_bus_example.event_bus import EventBus
from event_bus_example.publisher import StockPricePublisher, StockPriceConfig
from event_bus_example.event import PriceTickEvent
from event_bus_example.subscriber import LogPriceSubscriber


async def main():

    event_bus = EventBus()

    feeder = StockPricePublisher(bus=event_bus, config=StockPriceConfig())

    price_logger = LogPriceSubscriber()

    event_bus.subscribe(
        event_type=PriceTickEvent,
        handler=price_logger.log
    )

    feeder.stream()
