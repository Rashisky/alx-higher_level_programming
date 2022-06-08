#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_val = set()
    for k in my_list:
        uniq_val.add(k)
    return sum(uniq_val)
