def combo(a, b):
    """return the smallest of num with contain all digital order of a b

    >>> combo(531, 432)
    45312
    >>> combo(531, 4321)
    45321
    >>> combo(1234, 9123)
    91234
    """
    if min(a, b) == 0:
        return a + b
    elif a % 10 == b % 10:
        return combo(a // 10, b // 10) * 10 + a % 10
    else:
        return min(combo(a // 10, b) * 10 + a % 10, 
                   combo(a, b // 10) * 10 + b % 10)

