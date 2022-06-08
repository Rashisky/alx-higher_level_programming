#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for k, v in sorted(a_dictionary.items()):
        a.update({k: v*2})
    return a
