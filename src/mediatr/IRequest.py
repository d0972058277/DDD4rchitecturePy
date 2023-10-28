from typing import Generic, TypeVar

TResult = TypeVar("TResult")


class IRequest(Generic[TResult]):
    pass
