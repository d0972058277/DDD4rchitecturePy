from abc import ABC, abstractmethod
from typing import Iterable


class ValueObject(ABC):
    def __init__(self) -> None:
        if type(self) is ValueObject:
            raise TypeError("Cannot instantiate an abstract class")

        self._cached_hash_code = None

    @abstractmethod
    def _get_equality_components(self) -> Iterable:
        pass

    def __eq__(self, other) -> bool:
        if not isinstance(other, ValueObject):
            return False

        if type(self) != type(other):
            return False

        return list(self._get_equality_components()) == list(
            other._get_equality_components()
        )

    def __hash__(self) -> int:
        if self._cached_hash_code is None:
            self._cached_hash_code = hash(tuple(self._get_equality_components()))

        return self._cached_hash_code

    def __lt__(self, other) -> bool:
        if not isinstance(other, ValueObject):
            raise TypeError(f"Cannot compare {type(self)} and {type(other)}")

        if type(self) != type(other):
            raise TypeError("Cannot compare different types of ValueObject")

        return list(self._get_equality_components()) < list(
            other._get_equality_components()
        )

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __gt__(self, other) -> bool:
        return not self <= other

    def __ge__(self, other) -> bool:
        return not self < other
