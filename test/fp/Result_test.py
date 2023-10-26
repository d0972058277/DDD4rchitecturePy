import pytest
from src.fp import Result


def test_success():
    # Given
    result = Result.success()

    # When

    # Then
    assert result.is_success == True
    assert result.is_failure == False
    assert result.value == None
    with pytest.raises(RuntimeError):
        result.error


def test_success_with_value():
    # Given
    value = 1
    result = Result.success(value)

    # When

    # Then
    assert result.is_success == True
    assert result.is_failure == False
    assert result.value == value
    with pytest.raises(RuntimeError):
        result.error


def test_failure():
    # Given
    error_message = "Something went wrong"
    result = Result.failure(error_message)

    # When

    # Then
    assert result.is_success == False
    assert result.is_failure == True
    assert result.error == error_message
    with pytest.raises(RuntimeError):
        result.value
