import pytest
from source.primenumbers import get_n_primes


def test_should_return_all_primes_up_to_20():
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    result = get_n_primes(20)
    assert result == expected


def test_should_return_one_element_list_for_2():
    expected = [2]
    result = get_n_primes(2)
    assert result == expected


@pytest.mark.parametrize("input_value", [-1, 0, 1])
def test_should_return_empty_for_negatives_0_1(input_value):
    expected = []
    result = get_n_primes(input_value)
    assert result == expected
