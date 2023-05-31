import pytest
from source.primenumbers import is_prime


@pytest.mark.parametrize("input_value", [2, 5, 7, 251, 7919])
def test_should_return_true_for_prime(input_value):
    result = is_prime(input_value)
    assert result is True


@pytest.mark.parametrize("input_value", [4, 9, 18, 25])
def test_should_return_false_for_non_prime(input_value):
    result = is_prime(input_value)
    assert result is False


@pytest.mark.parametrize("input_value", [-1, 0, 1])
def test_should_return_false_for_negatives_0_1(input_value):
    result = is_prime(input_value)
    assert result is False
