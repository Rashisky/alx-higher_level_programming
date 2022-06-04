#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        Max = my_list[0]
        for u in my_list:
            if u > Max:
                Max = u
        return Max
