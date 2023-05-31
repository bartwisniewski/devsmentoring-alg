import pytest
from source.binary_search import find_x, generate_q_knowing_x


@pytest.mark.parametrize("px", [(6, 20), (1, 1), (2, 1), (135, 927)])
def test_should_return_x_if_possible(px):
    p, x = px
    q = generate_q_knowing_x(p, x)
    result = find_x(p, q)
    assert result == x


@pytest.mark.parametrize("px", [(6, 20), (1, 1), (2, 1), (135, 927)])
def test_should_return_none_if_impossible(px):
    p, x = px
    q = generate_q_knowing_x(p, x)+1
    result = find_x(p, q)
    assert result is None


def test_should_return_none_if_q_less_equal_p():
    result = find_x(6, 6)
    assert result is None
    result = find_x(6, 5)
    assert result is None
    result = find_x(1, 1)
    assert result is None
