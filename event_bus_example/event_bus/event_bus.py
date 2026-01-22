from collections import defaultdict
import logging
from typing import Callable, Type

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class EventBus:

    def __init__(self):
        self._event_type_to_handlers: dict[Type, list[Callable]] = (
            defaultdict(list))

    def subscribe(self, event_type: Type, handler: Callable):
        logger.info(f"Handler {handler} subscribed to event type: "
                    f"{type(event_type)}")
        self._event_type_to_handlers[event_type].append(handler)

    def publish(self, event: BaseModel):
        logger.info(f"Publishing event of type: {type(event)}")
        for handler in self._event_type_to_handlers[type(event)]:
            handler(event)
