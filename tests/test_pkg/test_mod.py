import pytest

from ciproj.pkg import mod


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    [
        [1, 1, 2],
        [0, 0, 0],
        [1, 0, 1]
    ]
)
def test_add(a, b, expected):
    assert mod.Calculator(a, b).add(a, b) == expected, '两者要相等'


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    [
        [1, 1, 0],
        [1, 0, 1]
    ]
)
def test_sub(a, b, expected):
    assert mod.Calculator(a, b).sub(a, b) == expected, '两者要相等'
