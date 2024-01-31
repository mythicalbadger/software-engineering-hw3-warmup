import pytest

from src.leetcode.fibonacci import fibonacci


def test_fibonacci_zero():
    """Tests that the 0th fibonacci number is 0."""
    assert fibonacci(0) == 0


def test_fibonacci_negative():
    """Tests that a negative number raises a ValueError."""
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_valid():
    """Tests that the first 10 fibonacci numbers are correct."""
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
