from abc import abstractmethod
from typing import Generic, TypeVar

from .INotification import INotification

TNotification = TypeVar("TNotification", bound=INotification)


class INotificationHandler(Generic[TNotification]):
    @abstractmethod
    async def handle_async(self, notification: TNotification) -> None:
        pass
