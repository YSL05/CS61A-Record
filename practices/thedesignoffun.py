"""the design of function"""

def cube(k):
    """
    the cube of k
    """
    assert k > 0, 'the input should be positive'
    return pow(k,3)

def id(k):
    return k

def summation(n, term):
    """sum the first n terms of a sequence

    >>> summation(5, cube)
    225
    >>> summation(5, id)
    15
    """
    total = 0
    k = 1
    while k <= n:
        total = total + term(k)
        k += 1
    return total