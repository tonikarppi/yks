import pytest
import yks


@pytest.mark.parametrize(
    "a, b, expected", [(-2, -1, -3), (-1, 0, -1), (0, 1, 1), (1, 2, 3)]
)
def test_plus(a, b, expected):
    assert yks.plus(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(-2, -1, -1), (-1, 0, -1), (0, 1, -1), (1, 2, -1)]
)
def test_minus(a, b, expected):
    assert yks.minus(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(-2, -1, 2), (-1, 0, 0), (0, 1, 0), (1, 2, 2)]
)
def test_times(a, b, expected):
    assert yks.times(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(-2, -1, 2), (0, 1, 0), (1, 2, 0.5)])
def test_divided_by(a, b, expected):
    assert yks.divided_by(a, b) == expected


@pytest.mark.parametrize("a, b", [(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)])
def test_divided_by_errors(a, b):
    with pytest.raises(ZeroDivisionError):
        assert yks.divided_by(a, b)


@pytest.mark.parametrize(
    "a, b, expected",
    [(-1, -1, -1), (-1, 0, 0), (0, -1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)],
)
def test_max_of(a, b, expected):
    assert yks.max_of(a, b) == expected


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], None),
        ([-1], -1),
        ([0], 0),
        ([1], 1),
        ([-1, -1], -1),
        ([-1, 0], 0),
        ([0, -1], 0),
        ([0, 0], 0),
        ([0, 1], 1),
        ([1, 0], 1),
        ([1, 1], 1),
    ],
)
def test_max_in(values, expected):
    assert yks.max_in(values) == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        (("add", "6", "2"), (True, "8")),
        (("subtract", "6", "2"), (True, "4")),
        (("multiply", "6", "2"), (True, "12")),
        (("divide", "6", "2"), (True, "3.0")),
        (
            ("multip", "6", "2"),  # Invalid operator
            (False, "Expected: yks <add|subtract|multiply|divide> <num1> <num2>."),
        ),
        (
            ("multiply", "a", "2"),  # Invalid operand 1
            (False, "Expected: yks <add|subtract|multiply|divide> <num1> <num2>."),
        ),
        (
            ("multiply", "6", "a"),  # Invalid operand 2
            (False, "Expected: yks <add|subtract|multiply|divide> <num1> <num2>."),
        ),
        (
            ("divide", "6", "0"),  # Divide by zero
            (False, "Division by zero encountered."),
        ),
    ],
)
def test_main_success(args, expected):
    assert yks.main(*args) == expected
