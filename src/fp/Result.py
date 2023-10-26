from typing import Generic, TypeVar


TValue = TypeVar("TValue")
TError = TypeVar("TError")


class Result(Generic[TValue, TError]):
    __is_success: bool
    __value: TValue
    __error: TError

    def __init__(self, is_success: bool, value: TValue, error: TError) -> None:
        self.__is_success = is_success
        self.__value = value
        self.__error = error

    @property
    def is_success(self) -> bool:
        return self.__is_success

    @property
    def is_failure(self) -> bool:
        return not self.__is_success

    @property
    def value(self) -> TValue:
        if not self.is_success:
            raise RuntimeError("Result is failure")
        return self.__value

    @property
    def error(self) -> TError:
        if self.is_success:
            raise RuntimeError("Result is success")
        return self.__error

    @staticmethod
    def success(value: TValue = None) -> "Result[TValue, None]":
        return Result(True, value, None)

    @staticmethod
    def failure(error: TError) -> "Result[None, TError]":
        return Result(False, None, error)
