import pytest
from source.recurency import crash_me


def test_should_raise_recursion_error():
    with pytest.raises(RecursionError):
        crash_me()
