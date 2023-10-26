from abc import ABC
from src.fp.IResult import IResult, IValue, IError


class Result(IResult, IValue, IError, ABC):
    __is_success: bool
    __value: any
    __error: any

    def __init__(self, is_success: bool, value: any, error: any) -> None:
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
    def value(self) -> any:
        if not self.is_success:
            raise RuntimeError("Result is failure")
        return self.__value

    @property
    def error(self) -> any:
        if self.is_success:
            raise RuntimeError("Result is success")
        return self.__error

    @staticmethod
    def success(value: any = None) -> "Result":
        return Result(True, value, None)

    @staticmethod
    def failure(error: any) -> "Result":
        return Result(False, None, error)
