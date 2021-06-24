import pytest
from solution import magic_tuples

def test_zeroes():
    assert list(magic_tuples(0, 0)) == []

@pytest.mark.parametrize('total,maxval',
                         [(3,3),
                          (5,5),
                          (30, 70)])
def test_basic(total, maxval):
    result = list(magic_tuples(total,maxval))

    assert all([t[0] <= maxval and t[1] <= maxval
                for t in result])
    assert all([sum(t) == total
                for t in result])

def test_is_iterator():
    result = magic_tuples(10, 10)
    assert iter(result) == result

def test_impossible():
    result = list(magic_tuples(100, 3))
