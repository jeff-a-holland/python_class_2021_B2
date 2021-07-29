#!/Users/jeff/.pyenv/shims/python

from solution import mygetter

def test_one_pos_index():
    s = 'abcde'
    i2 = mygetter(2)

    assert i2(s) == 'c'

def test_one_neg_index():
    s = 'abcde'
    i2 = mygetter(-2)

    assert i2(s) == 'd'

def test_one_key():
    d = {'a':1, 'b':2, 'c':3}
    ka = mygetter('a')

    assert ka(d) == 1

def test_multiple_indexes():
    s = 'abcde'
    i21 = mygetter(2,1)

    assert i21(s) == ('c', 'b')

def test_multiple_keys():
    d = {'a':1, 'b':2, 'c':3}
    kab = mygetter('a', 'b')

    assert kab(d) == (1, 2)
