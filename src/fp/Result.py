from src.fp.IResult import IResultBase


class Result(IResultBase):
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
        return self.__value

    @property
    def error(self) -> any:
        return self.__error

    @staticmethod
    def success(value: any = None) -> IResultBase:
        return Result(True, value, None)

    @staticmethod
    def failure(error: any) -> IResultBase:
        return Result(False, None, error)
