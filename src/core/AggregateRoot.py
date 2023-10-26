from abc import ABC
from typing import List, TypeVar
from src.core import IDomainEvent
from src.core import Entity


TId = TypeVar("TId", bound=any)


class AggregateRoot(Entity[TId], ABC):
    __domain_events: List[IDomainEvent]

    def __init__(self, id: TId = None) -> None:
        if type(self) is AggregateRoot:
            raise TypeError("Cannot instantiate an abstract class")

        super().__init__(id)
        self.__domain_events = []

    @property
    def domain_events(self) -> List[IDomainEvent]:
        return self.__domain_events.copy()

    def _add_domain_event(self, domain_event: IDomainEvent) -> None:
        self.__domain_events.append(domain_event)

    def clear_domain_events(self) -> None:
        self.__domain_events.clear()
