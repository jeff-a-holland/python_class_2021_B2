#!/Users/jeff/.pyenv/shims/python

"""Magic Tuples generator function"""
def magic_tuples(arg1, arg2):
    for int1 in range(1,arg1 + 1):
        for int2 in range(1, arg1 + 1):
            if (int1 + int2 == arg1) and (int1 < arg2) and (int2 < arg2):
                tuple = (int1, int2)
                yield tuple

"""Testing"""
for t in magic_tuples(10,8):
    print(t)
