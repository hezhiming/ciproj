
from ciproj.pkg import mod
import pytest

@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    [
        [1, 1, 2],
        [0, 0, 0],
        [1, 0, 0]
    ]
)
def test_add(a, b, expected):
    assert mod.Calculator(a, b) == expected, '两者要相等'


def test_sub():
    assert False
