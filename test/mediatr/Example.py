from typing import TypeVar
from mediatr import (
    IRequest,
    IRequestHandler,
    register_handler,
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


@register_handler
class NoneExampleRequestHandler(IRequestHandler[NoneExampleRequest]):
    async def handle_async(self, request: NoneExampleRequest) -> None:
        return None


@register_handler
class IntExampleRequestHandler(IRequestHandler[IntExampleRequest]):
    async def handle_async(self, request: IntExampleRequest) -> int:
        return request.value
