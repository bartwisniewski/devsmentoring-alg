from source.sorting import bubble, insertion_sort, quicksort


def test_should_sort_using_bubble():
    array = [5, 1, 8, 2, 5]
    expected = [1, 2, 5, 5, 8]
    bubble(array)

    assert array == expected


def test_should_sort_using_insertion():
    array = [5, 1, 8, 2, 5]
    expected = [1, 2, 5, 5, 8]
    insertion_sort(array)
    assert array == expected


def test_should_sort_using_quicksort():
    array = [5, 1, 8, 2, 5]
    expected = [1, 2, 5, 5, 8]
    quicksort(array)
    assert array == expected
