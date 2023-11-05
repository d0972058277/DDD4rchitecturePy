from typing import TypeVar
from mediatr import (
    INotification,
    INotificationHandler,
    IRequest,
    IRequestHandler,
    Mediator,
)

TService = TypeVar("TService")


class NoneExampleRequest(IRequest[None]):
    pass


class IntExampleRequest(IRequest[int]):
    __value: int

    def __init__(self, value: int) -> None:
        super().__init__()
        self.__value = value

    @property
    def value(self):
        return self.__value


class ExampleNotification(INotification):
    pass


@Mediator.register_handler
class NoneExampleRequestHandler(IRequestHandler[NoneExampleRequest]):
    async def handle_async(self, request: NoneExampleRequest) -> None:
        return None


@Mediator.register_handler
class IntExampleRequestHandler(IRequestHandler[IntExampleRequest]):
    async def handle_async(self, request: IntExampleRequest) -> int:
        return request.value


@Mediator.register_handler
class AExampleNotificationHandler(INotificationHandler[ExampleNotification]):
    async def handle_async(self, notification: ExampleNotification) -> None:
        pass


@Mediator.register_handler
class BExampleNotificationHandler(INotificationHandler[ExampleNotification]):
    async def handle_async(self, notification: ExampleNotification) -> None:
        pass
