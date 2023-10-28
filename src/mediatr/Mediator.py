from inspect import signature
from typing import Any, Dict, Type, TypeVar

from .IRequest import IRequest
from .IRequestHandler import IRequestHandler
from .IServiceProvider import IServiceProvider
from .IMediator import IMediator

TResult = TypeVar("TResult")
TRequestHandler = TypeVar("TRequestHandler", bound=IRequestHandler[Any])

__handlers__: Dict[Type[IRequest[Any]], Type[IRequestHandler[Any]]] = {}


class Mediator(IMediator):
    __service_provider: IServiceProvider

    def __init__(self, service_provider: IServiceProvider) -> None:
        super().__init__()
        self.__service_provider = service_provider

    async def send_async(self, request: IRequest[TResult]) -> TResult:
        request_type = type(request)
        handler_type = __handlers__[request_type]
        handler = self.__service_provider.GetRequiredService(handler_type)
        result = await handler.handle_async(request)
        return result


# Decorator function to register request handler types
def register_handler(handler_cls: Type[TRequestHandler]) -> Type[TRequestHandler]:
    request_type = signature(handler_cls.handle_async).parameters["request"].annotation
    if not __handlers__.get(request_type):
        __handlers__[request_type] = handler_cls
    return handler_cls
