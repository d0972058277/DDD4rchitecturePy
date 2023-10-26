from typing import Generic, TypeVar

TValue = TypeVar("TValue")


class Maybe(Generic[TValue]):
    __is_value_set: bool
    __value: TValue

    def __init__(self, value: TValue) -> None:
        if value is None:
            self.__is_value_set = False
        else:
            self.__is_value_set = True

        self.__value = value

    @property
    def has_value(self) -> bool:
        return self.__is_value_set

    @property
    def has_no_value(self) -> bool:
        return not self.__is_value_set

    @property
    def value(self) -> TValue:
        if not self.__is_value_set:
            raise RuntimeError("Maybe has no value")
        return self.__value

    @staticmethod
    def has(value: TValue) -> "Maybe[TValue]":
        return Maybe(value)

    @staticmethod
    def none() -> "Maybe[None]":
        return Maybe(None)
