from abc import ABC, abstractmethod
from typing import TypeVar

from .IRequest import IRequest

TResult = TypeVar("TResult")


class IMediator(ABC):
    @abstractmethod
    async def send_async(self, request: IRequest[TResult]) -> TResult:
        pass
