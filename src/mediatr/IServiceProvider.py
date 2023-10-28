from abc import ABC, abstractmethod
from typing import Type, TypeVar

TService = TypeVar("TService")


class IServiceProvider(ABC):
    @abstractmethod
    def GetService(self, service_type: Type[TService]) -> TService | None:
        pass

    @abstractmethod
    def GetRequiredService(self, service_type: Type[TService]) -> TService:
        pass
