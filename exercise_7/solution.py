#!/Users/jeff/.pyenv/shims/python
import time

class TooSoonError(Exception):
    """Custom Exception"""
    def __init__(self, value):
        message = f'Wait another {value} seconds'
        super().__init__(message)

## Set start_time global var
start_time = time.time()

def once_per_minute(func):
    """Decorator function that only allows a function passed as an arg to run
    once a minute."""
    def wrapper(*args):
        global start_time
        delta = 60 - (time.time() - start_time)

        ## Create arg_str to handle multiple args of different types given to
        ## the decorated function.
        arg_list = [str(value) for value in args]
        arg_str = ' '.join(arg_list)

        if i == 0:
            return func(arg_str)
        elif i > 0 and delta > 0:
            raise TooSoonError(delta)
        else:
            start_time = time.time()
            return func(arg_str)
    return wrapper

@once_per_minute
def hello(name):
    return "Hello, {}".format(name)

for i in range(30):
    try:
        time.sleep(3)
        ## STDOUT that works with pytest code.
        print(hello("attempt {}".format(i)))
        ## Test multiple args of different types. Will not work with pytest code.
        #print(hello([1,2,3], 'jeff'))
    except TooSoonError as e:
        print("Too soon: {}".format(e))
