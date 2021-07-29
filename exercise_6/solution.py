#!/Users/jeff/.pyenv/shims/python

def mygetter(*args):
    """Function for mygetter, which implements the functionality of the
    itemgetter method of the operator module."""

    args_list = [item for item in args]

    def getitems(arg):
        """Function for returning a function (getitems) that prints a tuple for
        multiple values, or a string for a single value, based on the cardinality
        of the arguments passed into mygetter."""

        value_list = []
        for value in args_list:
            value_list.append(arg[value])
        if len(value_list) == 1:
            return value_list[0]
        else:
            return tuple(value_list)
    return getitems

def main():
    """Main function for mygetter implemntation"""

    ### Prints:  (5, 6)
    g1 = mygetter(0, 1)
    print(g1([5,6,7]),'\n')

    ## Prints: ('a', 'g')
    g2 = mygetter(0, -1)
    print(g2(('a','b','c','d','e','f','g')),'\n')

    ## Prints:  3
    g3 = mygetter('beets')
    print(g3({'apples': 4, 'beets': 3, 'cherries': 5}),'\n')

    ## Prints: (1, 5)
    g4 = mygetter('hi', 'doing')
    print(g4({'hi': 1, 'how': 2, 'are': 3, 'you': 4, 'doing': 5}),'\n')

    ## Prints:  ('b', 'd')
    g5 = mygetter(1, 3)
    print(g5('abcde'),'\n')

if __name__ == '__main__':
    main()
