def add_integers(n1, n2):
    '''Adds two integers

    Raises  TypeError if a non-integer is passed as an argument
    :param n1: the first number
    :param n2: the second number
    '''
    assert_int(n1)
    assert_int(n2)
    return n1 + n2

def assert_int(n):
    '''Raises TypeError if number is not integer'''
    tmp = "{} is not type int"
    if not isinstance(n, int):
        raise TypeError(tmp.format(n))



