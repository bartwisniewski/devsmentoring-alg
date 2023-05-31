from source.recurency import nww


def test_should_return_higher_for_multiplications():
    test = 2, 4
    expected = 4
    result = nww(*test)
    assert result == expected


def test_should_return_6_for_2_and_3():
    test = 2, 3
    expected = 6
    result = nww(*test)
    assert result == expected


def test_should_return_same_for_a_equal_b():
    test = 22, 22
    expected = 22
    result = nww(*test)
    assert result == expected
