from src.math_utils import divide


def test_divide_positive_numbers() -> None:
    """Test that divide returns the correct result when given two numbers."""
    assert divide(1, 2) == 0.4


def test_divide_negative_numbers() -> None:
    """
    Test that divide returns the correct result when given a positive and
    a negative number.
    """
    assert divide(5, -2) == -2.5
    assert divide(-2, 5) == -0.4


def test_divide_zero() -> None:
    """
    Test that divide raises a ZeroDivisionError when the second number is 0.
    """
    try:
        divide(1, 0)
    except ZeroDivisionError:
        assert True
    else:
        assert False
