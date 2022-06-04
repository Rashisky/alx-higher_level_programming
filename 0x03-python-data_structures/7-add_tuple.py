#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    c = [x for x in tuple_a]
    d = [y for y in tuple_b]
    while (len(c) < 2 or len(d) < 2):
        c.append(0) if len(c) < 2 else d.append(0)
    result = c[0] + d[0], c[1] + d[1]
    return result
