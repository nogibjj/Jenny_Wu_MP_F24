"""To test, import the written function from the main.py file """

from main import multiply


def test_multiply():
    """Here we are asserting that 2*2 equals to 4"""
    assert multiply(2, 2) == 4
    assert multiply(3, 2) == 6
    assert multiply(4, 2) == 8


if __name__ == "__main__":
    test_multiply()
