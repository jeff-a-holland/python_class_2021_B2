#!/Users/jeff/.pyenv/shims/python

import unicodedata

def str_range(start, end, *args):
    """Function to mimic range function in standar python library. Both start
    and end values are mandatory, step value as the third arg is optional. The
    step value must be an int (positive or negative) and not 0 or 1, otherwise
    a TypeError excpetion is raised."""

    step_val = 1
    if len(args) == 1 and isinstance(args[0], int) \
                      and (args[0] != 0 and args[0] != 1):
        step_val = args[0]
    elif len(args) == 0:
        pass
    else:
        raise TypeError('No more than 3 args can be suplied to str_range, and 3rd arg must a non-zero "int" and not "1"')

    # Get the normalized int value for the character from the unicodedata module
    start_num = [ord(c) for c in unicodedata.normalize('NFC', start)]
    end_num = [ord(c) for c in unicodedata.normalize('NFC', end)]

    # Determine the number of chars betwen the start and end args (including the
    # start and end chars) and the step_val arg (if supplied)
    if step_val % 2 == 0:
        length = abs(int((abs(start_num[0] - end_num[0]) + 2) / step_val))
    else:
        length = abs(int((abs(start_num[0] - end_num[0]) + 1) / step_val))

    if step_val > length:
        raise TypeError('Step value cannot be greater than the cardinality of the chars between start char and end char')

    counter = 0
    char_str = ''
    while counter < length:
        char_str += chr(start_num[0] + step_val * counter)
        counter += 1
    print(char_str)
    return(iter(char_str))

## prints: a
str_range('a', 'a')
## prints: ace
str_range('a', 'f', 2)
## prints: ac
str_range('a', 'c', 2)
## prints: ca
str_range('c', 'a', -2)
## prints: TypeError: Step value cannot be greater than the cardinality of the
##                    chars between start char and end char
#str_range('c', 'a', 3)  #Commenting out for pytest. Uncomment to test standalone
