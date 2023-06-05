from source.linked_lists import LinkedList


def test_should_create_a_linked_list():
    inputs = [1, 5, 5, 1, 4, 2]
    expected = '1, 5, 5, 1, 4, 2'
    my_list = LinkedList()
    for _input in inputs:
        my_list.append(_input)
    assert my_list.__str__() == expected


def test_should_clean_list_from_repeating_numbers():
    inputs = [1, 5, 5, 1, 4, 2]
    expected = '1, 5, 4, 2'
    my_list = LinkedList()
    for _input in inputs:
        my_list.append(_input)
    my_list.clean()
    assert my_list.__str__() == expected
