from abc import ABC
from typing import TypeVar, Generic

TId = TypeVar("TId")


class Entity(ABC, Generic[TId]):
    """Abstract base class for entities."""

    _id: TId

    def __init__(self, id: TId = None) -> None:
        """Initialize a new entity.
        Args:
            id: The unique identifier of the entity.
        """
        if type(self) is Entity:
            raise TypeError("Cannot instantiate an abstract class")

        self._id = id

    @property
    def id(self) -> TId:
        """Get the unique identifier of the entity."""
        return self._id

    def __eq__(self, other: object) -> bool:
        """Check if two entities are equal.

        Args:
            other: The other entity to compare to.

        Returns:
            True if the two entities are equal, False otherwise.
        """
        if self is other:
            return True

        if type(self) != type(other):
            return False

        if not issubclass(type(other), Entity):
            return False

        if not isinstance(other, Entity):
            return False

        return self.id == other.id  # type: ignore

    def __ne__(self, other: object) -> bool:
        """Check if two entities are not equal."""
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """Get the hash value of the entity."""
        return hash(f"{type(self).__qualname__}({self.id})")

    def __lt__(self, other: object) -> bool:
        """Compare two entities based on their IDs."""
        if other is None:
            return False

        if self is other:
            return False

        return self.id < other.id  # type: ignore

    def __le__(self, other: object) -> bool:
        """Compare two entities based on their IDs."""
        return self == other or self < other

    def __gt__(self, other: object) -> bool:
        """Compare two entities based on their IDs."""
        if other is None:
            return False

        if self is other:
            return False

        return self.id > other.id  # type: ignore

    def __ge__(self, other: object) -> bool:
        """Compare two entities based on their IDs."""
        return self == other or self > other
