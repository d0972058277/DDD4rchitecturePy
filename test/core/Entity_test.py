import pytest
from core import Entity


class ExampleEntity1(Entity[int]):
    def __init__(self, id: int) -> None:
        super().__init__(id)


class ExampleEntity2(Entity[int]):
    def __init__(self, id: int) -> None:
        super().__init__(id)


def test_entity_equality():
    # Given
    entity1 = ExampleEntity1(1)
    entity2 = ExampleEntity1(1)
    entity3 = ExampleEntity1(2)
    entity4 = ExampleEntity2(1)

    # When

    # Then
    assert entity1 == entity2
    assert entity1 != entity3
    assert entity2 != entity3
    assert entity4 != entity1


def test_entity_ordering():
    # Given
    entity1 = ExampleEntity1(1)
    entity2 = ExampleEntity1(2)
    entity3 = ExampleEntity1(3)

    # When

    # Then
    assert entity1 < entity2
    assert entity2 > entity1
    assert entity2 < entity3
    assert entity3 > entity2
    assert entity1 <= entity2
    assert entity2 >= entity1
    assert entity2 <= entity3
    assert entity3 >= entity2


def test_entity_hash():
    # Given
    entity1 = ExampleEntity1(1)
    entity2 = ExampleEntity1(2)

    # When

    # Then
    assert hash(entity1) == hash(f"ExampleEntity1(1)")
    assert hash(entity2) == hash(f"ExampleEntity1(2)")


def test_cannot_instantiate_abstract_class():
    # Assert
    with pytest.raises(TypeError):
        Entity(1)
