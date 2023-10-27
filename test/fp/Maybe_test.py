import pytest
from fp import Maybe


def test_has_value():
    # Given
    maybe_int = Maybe.has(42)
    maybe_null = Maybe.has(None)
    maybe_none = Maybe.none()

    # When

    # Then
    assert maybe_int.has_value == True
    assert maybe_null.has_value == False
    assert maybe_none.has_value == False


def test_has_no_value():
    # Given
    maybe_int = Maybe.has(42)
    maybe_null = Maybe.has(None)
    maybe_none = Maybe.none()

    # When

    # Then
    assert maybe_int.has_no_value == False
    assert maybe_null.has_no_value == True
    assert maybe_none.has_no_value == True


def test_get_value():
    # Given
    int_value = 42
    maybe_int = Maybe.has(int_value)
    maybe_null = Maybe.has(None)
    maybe_none = Maybe.none()

    # When

    # Then
    assert maybe_int.value == int_value
    with pytest.raises(RuntimeError):
        maybe_null.value
    with pytest.raises(RuntimeError):
        maybe_none.value
