import pytest
from pytest_mock import MockerFixture

from mediatr import IMediator, IServiceProvider, Mediator
from .Example import *


@pytest.fixture
def service_provider(mocker: MockerFixture) -> IServiceProvider:
    mock = mocker.Mock(IServiceProvider)

    def get_service(handler_type: type):
        if handler_type is NoneExampleRequestHandler:
            return NoneExampleRequestHandler()
        if handler_type is IntExampleRequestHandler:
            return IntExampleRequestHandler()
        if handler_type is IMediator:
            return Mediator(mock)

    def get_required_service(handler_type: type):
        if handler_type is NoneExampleRequestHandler:
            return NoneExampleRequestHandler()
        if handler_type is IntExampleRequestHandler:
            return IntExampleRequestHandler()
        if handler_type is IMediator:
            return Mediator(mock)
        raise RuntimeError()

    mock.GetService.side_effect = get_service
    mock.GetRequiredService.side_effect = get_required_service

    return mock


@pytest.fixture
def mediator(service_provider: IServiceProvider) -> IMediator:
    return service_provider.GetRequiredService(IMediator)


async def test_none_request_handler(mediator: IMediator):
    # Given
    request = NoneExampleRequest()

    # When
    result = await mediator.send_async(request)

    # Then
    assert result is None


async def test_int_request_handler(mediator: IMediator):
    # Given
    request = IntExampleRequest(42)

    # When
    result = await mediator.send_async(request)

    # Then
    assert result == 42


async def test_handler(service_provider: IServiceProvider):
    # Given
    none_handler = service_provider.GetRequiredService(NoneExampleRequestHandler)
    int_handler = service_provider.GetRequiredService(IntExampleRequestHandler)

    # When
    none_result = await none_handler.handle_async(NoneExampleRequest())
    int_result = await int_handler.handle_async(IntExampleRequest(1))

    # Then

    assert none_result == None
    assert int_result == 1
