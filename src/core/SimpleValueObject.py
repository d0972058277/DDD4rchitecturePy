from abc import ABC
from typing import Iterable
from .ValueObject import ValueObject


class SimpleValueObject(ValueObject, ABC):
    __value: any

    def __init__(self, value: any) -> None:
        if type(self) is SimpleValueObject:
            raise TypeError("Cannot instantiate an abstract class")

        super().__init__()
        self.__value = value

    def _get_equality_components(self) -> Iterable:
        yield self.__value

    @property
    def value(self):
        return self.__value
