import pytest
from core import SimpleValueObject


class ExampleValueObject(SimpleValueObject):
    def __init__(self, value: int) -> None:
        super().__init__(value)


def test_equality():
    # Given
    obj1 = ExampleValueObject(42)
    obj2 = ExampleValueObject(42)
    obj3 = ExampleValueObject(43)

    # When

    # Then
    assert obj1 == obj2  # 相同值的物件應該相等
    assert not obj1 == obj3  # 不同值的物件應該不相等


def test_inequality():
    # Given
    obj1 = ExampleValueObject(42)
    obj2 = ExampleValueObject(42)
    obj3 = ExampleValueObject(43)

    # When

    # Then
    assert not obj1 != obj2  # 相同值的物件不應該不相等
    assert obj1 != obj3  # 不同值的物件應該不相等


def test_hash():
    # Given
    obj1 = ExampleValueObject(42)
    obj2 = ExampleValueObject(42)

    # When

    assert hash(obj1) == hash(obj2)  # 相同值的物件應該具有相同的哈希值


def test_comparison():
    # Given
    obj1 = ExampleValueObject(42)
    obj2 = ExampleValueObject(43)

    # When

    # Then
    assert obj1 < obj2
    assert obj1 <= obj2
    assert not obj1 > obj2
    assert not obj1 >= obj2


def test_type_check():
    # Given
    obj1 = ExampleValueObject(42)
    obj2 = "not a ValueObject"

    # When

    # Then
    with pytest.raises(TypeError):
        obj1 == obj2  # 與非 ValueObject 比較應引發 TypeError
        obj1 < obj2  # 與非 ValueObject 比較應引發 TypeError


def test_cannot_instantiate_abstract_class():
    # Assert
    with pytest.raises(TypeError):
        SimpleValueObject(1)
