import pytest
from source.binary_search import count_higher


def test_should_return_true_if_there_is_more():
    test = [21] * 11
    test += [20] * 19
    result = count_higher(test, 20, 10)
    assert result is True


def test_should_return_true_if_there_is_exact():
    test = [21] * 10
    test += [20] * 20
    result = count_higher(test, 20, 10)
    assert result is True


def test_should_return_false_if_there_is_less():
    test = [21] * 9
    test += [20] * 21
    result = count_higher(test, 20, 10)
    assert result is False
