from abc import ABC, abstractmethod
from typing import TypeVar

from .IRequest import IRequest
from .INotification import INotification

TResult = TypeVar("TResult")


class IMediator(ABC):
    @abstractmethod
    async def send_async(self, request: IRequest[TResult]) -> TResult:
        pass

    @abstractmethod
    async def publish_async(self, notification: INotification) -> None:
        pass
