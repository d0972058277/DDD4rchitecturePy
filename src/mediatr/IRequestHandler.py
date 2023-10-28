from abc import abstractmethod
from typing import Any, Generic, TypeVar

from .IRequest import IRequest

TRequest = TypeVar("TRequest", bound=IRequest[Any])


class IRequestHandler(Generic[TRequest]):
    @abstractmethod
    async def handle_async(self, request: TRequest) -> Any:
        pass
