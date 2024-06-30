def perfixs(s):
    if s:
        for x in perfixs(s[:-1]):
            yield x
        yield s    

