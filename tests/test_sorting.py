from source.sorting import bubble, insertion_sort, quicksort, merge_sort


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


def test_should_sort_using_mergesort():
    array = [5, 1, 8, 2, 5, 10, 3, 6, 8]
    expected = [1, 2, 3, 5, 5, 6, 8, 8, 10]
    merge_sort(array)
    assert array == expected
