from sqdiv import divisors, n_rows_cols
from hypothesis import given
from hypothesis.strategies import integers
import numpy as np


@given(integers(min_value=1, max_value=10000))
def test_divisors(x):
    divs = divisors(x)
    # 1 should always be a divisor
    assert 1 in divs
    # divs should always be a list
    assert isinstance(divs, list)
    # the maximum value in divs should always less than or equal to the square
    # root of x
    assert max(divs) <= np.sqrt(x)


@given(integers(min_value=1, max_value=10000))
def test_n_rows_cols(x):
    nrows, ncols = n_rows_cols(x)
    # nrows, ncols should always be positive
    assert nrows > 0
    assert ncols > 0


@given(integers(min_value=1, max_value=10000))
def test_n_rows_cols_squared(x):
    nrows, ncols = n_rows_cols(x, squared=True)
    assert nrows == ncols
