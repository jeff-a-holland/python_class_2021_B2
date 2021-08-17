#!/Users/jeff/.pyenv/shims/python

class Foo(object):
    """Implement eq, hash, and str methods to make the Foo class return a unique
    value only once when tyring to add to a set multiple times"""
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash((self.x))

    def __str__(self):
        return f'{self.x}'

class Uniquish(object):
    """Implement eq, hash, and str methods to make the Uniquish class return a
    unique value only once when tyring to add to a set multiple times"""
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash((self.x))

    def __str__(self):
        return f'{self.x}'

## Test Foo class. Should return a set of length 1.
f1 = Foo(10)
f2 = Foo(10)
f3 = Foo(10)
s = {f1, f2, f3}
print('\nFoo result:', s)

## Test Uniquish class by creating Bar class and inherit Uniquish class. Should
## return a set of length 1.
class Bar(Uniquish):
    def __init__(self, x, y):
        self.x = x
        self.y = y
b1 = Bar(10, 'abc')
b2 = Bar(10, 'abc')
b3 = Bar(10, 'abc')
s = {b1, b2, b3}
print('\nUniquish result:', s, '\n')
