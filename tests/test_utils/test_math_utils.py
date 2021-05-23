from ciproj.utils import math_utils
import pytest


@pytest.mark.parametrize(
    ['a', 'b', 'expected'],
    [
        [0, 0, 0],
        [1, 1, 2],
    ]
)
def test_add(a, b, expected):
    assert math_utils.add(a, b) == expected

