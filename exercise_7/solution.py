#!/Users/jeff/.pyenv/shims/python
import time

class TooSoonError(Exception):
    """Custom Exception"""
    def __init__(self, value):
        message = f'Wait another {value} seconds'
        super().__init__(message)

start_time = time.time()
def once_per_minute(func):
    """Decorator function that only allows a function passed as an arg to run
    once a minute."""
    def wrapper(*args):
        global start_time
        delta = 60 - (time.time() - start_time)

        if i == 0:
            return func(args[0])
        elif i > 0 and delta > 0:
            raise TooSoonError(delta)
        else:
            start_time = time.time()
            return func(args[0])
    return wrapper

@once_per_minute
def hello(name):
    return "Hello, {}".format(name)

for i in range(30):
    try:
        time.sleep(3)
        print(hello("attempt {}".format(i)))
    except TooSoonError as e:
        print("Too soon: {}".format(e))
