import pytest
from source.recurency import count_vowels


def test_should_count_vowels_correctly():
    test_string = 'baadace'
    expected = {'a': 3, 'e': 1}
    result = count_vowels(test_string)
    assert result == expected


def test_should_return_dict():
    test_string = 'baadace'
    result = count_vowels(test_string)
    assert type(result) == dict


def test_should_empty_dict_for_empty_string_input():
    test_string = ''
    result = count_vowels(test_string)
    assert result == {}
