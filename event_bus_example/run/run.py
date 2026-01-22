import asyncio

from event_bus_example.event_bus import EventBus
from event_bus_example.publisher import StockPriceFeed, StockPriceConfig
from event_bus_example.event import PriceTick
from event_bus_example.consumer import PriceLogger


async def main():

    event_bus = EventBus()

    feeder = StockPriceFeed(bus=event_bus, config=StockPriceConfig())

    price_logger = PriceLogger()

    event_bus.subscribe(
        event_type=PriceTick,
        handler=price_logger.log
    )

    feeder.stream()


if __name__ == "__main__":
    asyncio.run(main())
