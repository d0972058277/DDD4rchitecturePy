from inspect import signature
from typing import Any, Dict, List, Type, TypeVar

from .IRequest import IRequest
from .IRequestHandler import IRequestHandler
from .INotification import INotification
from .INotificationHandler import INotificationHandler
from .IServiceProvider import IServiceProvider
from .IMediator import IMediator

TResult = TypeVar("TResult")
TRequest = TypeVar("TRequest", bound=IRequest[Any])
TRequestHandler = TypeVar("TRequestHandler", bound=IRequestHandler[Any])
TNotification = TypeVar("TNotification", bound=INotification)
TNotificationHandler = TypeVar("TNotificationHandler", bound=INotificationHandler[Any])


class Mediator(IMediator):
    __service_provider: IServiceProvider
    __static_request_handlers: Dict[Type[IRequest[Any]], Type[IRequestHandler[Any]]] = {}
    __static_notification_handlers: Dict[Type[INotification], List[Type[INotificationHandler[Any]]]] = {}

    def __init__(self, service_provider: IServiceProvider) -> None:
        super().__init__()
        self.__service_provider = service_provider

    async def send_async(self, request: IRequest[TResult]) -> TResult:
        request_type = type(request)
        handler_type = Mediator.__static_request_handlers[request_type]

        handler = self.__service_provider.GetRequiredService(handler_type)
        result = await handler.handle_async(request)

        return result

    async def publish_async(self, notification: INotification) -> None:
        notification_type = type(notification)
        handler_types = Mediator.__static_notification_handlers[notification_type]

        for handler_type in handler_types:
            handler = self.__service_provider.GetRequiredService(handler_type)
            await handler.handle_async(notification)

    @staticmethod
    def register_handler(
        handler_type: Type[TRequestHandler] | Type[TNotificationHandler],
    ) -> Type[TRequestHandler] | Type[TNotificationHandler]:
        if issubclass(handler_type, IRequestHandler):
            request_type = signature(handler_type.handle_async).parameters["request"].annotation
            Mediator.register_request_handler(request_type, handler_type)

        # handler_cls is INotificationHandler
        else:
            notification_type = signature(handler_type.handle_async).parameters["notification"].annotation
            Mediator.register_notification_handler(notification_type, handler_type)

        return handler_type

    @staticmethod
    def register_request_handler(request_type: Type[TRequest], handler_type: Type[TRequestHandler]) -> None:
        if not Mediator.__static_request_handlers.get(request_type):
            Mediator.__static_request_handlers[request_type] = handler_type

    @staticmethod
    def register_notification_handler(notification_type: Type[TNotification], handler_type: Type[TNotificationHandler]) -> None:
        if not Mediator.__static_notification_handlers.get(notification_type):
            Mediator.__static_notification_handlers[notification_type] = []
        Mediator.__static_notification_handlers[notification_type].append(handler_type)
