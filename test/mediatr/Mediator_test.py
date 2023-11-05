from typing import cast
from unittest import mock

from mediatr import IServiceProvider, Mediator
from .Example import *


async def test_request_handler():
    # Given
    none_handler = NoneExampleRequestHandler()
    int_handler = IntExampleRequestHandler()

    # When
    none_result = await none_handler.handle_async(NoneExampleRequest())
    int_result = await int_handler.handle_async(IntExampleRequest(1))

    # Then

    assert none_result == None
    assert int_result == 1


async def test_send_none_request():
    # Given
    service_provider = cast(IServiceProvider, mock.Mock(spec=IServiceProvider))
    service_provider.GetRequiredService = mock.Mock(wraps=IServiceProvider.GetRequiredService, side_effect=lambda service_type: NoneExampleRequestHandler())  # type: ignore
    mediator = Mediator(service_provider)

    request = NoneExampleRequest()

    # When
    result = await mediator.send_async(request)

    # Then
    assert result is None
    service_provider.GetRequiredService.assert_called_with(NoneExampleRequestHandler)


async def test_send_int_request():
    # Given
    request = IntExampleRequest(42)
    service_provider = cast(IServiceProvider, mock.Mock(spec=IServiceProvider))
    service_provider.GetRequiredService = mock.Mock(wraps=IServiceProvider.GetRequiredService, side_effect=lambda service_type: IntExampleRequestHandler())  # type: ignore
    mediator = Mediator(service_provider)

    # When
    result = await mediator.send_async(request)

    # Then
    assert result == 42
    service_provider.GetRequiredService.assert_called_with(IntExampleRequestHandler)


async def test_publish_example_notification():
    # Given
    aExampleNotificationHandler = AExampleNotificationHandler()
    aExampleNotificationHandler.handle_async = mock.Mock(wraps=AExampleNotificationHandler.handle_async, side_effect=aExampleNotificationHandler.handle_async)

    bExampleNotificationHandler = BExampleNotificationHandler()
    bExampleNotificationHandler.handle_async = mock.Mock(wraps=BExampleNotificationHandler.handle_async, side_effect=bExampleNotificationHandler.handle_async)

    def get_required_service(service_type: type):
        if service_type is AExampleNotificationHandler:
            return aExampleNotificationHandler
        elif service_type is BExampleNotificationHandler:
            return bExampleNotificationHandler
        else:
            raise NotImplementedError()

    service_provider = cast(IServiceProvider, mock.Mock(spec=IServiceProvider))
    service_provider.GetRequiredService = mock.Mock(wraps=IServiceProvider.GetRequiredService, side_effect=get_required_service)

    notification = ExampleNotification()
    mediator = Mediator(service_provider)

    # When
    await mediator.publish_async(notification)

    # Then
    expected_calls = [mock.call(AExampleNotificationHandler), mock.call(BExampleNotificationHandler)]
    service_provider.GetRequiredService.assert_has_calls(expected_calls, any_order=True)
    aExampleNotificationHandler.handle_async.assert_called_once()
    bExampleNotificationHandler.handle_async.assert_called_once()
