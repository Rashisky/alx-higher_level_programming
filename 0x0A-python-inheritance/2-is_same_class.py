#!/usr/bin/python3
""" Function returns True if the object is
exactly an instance of the specified class, else
returns False
"""


def is_same_class(obj, a_class):
    """ Comparison function """
    if isinstance(type(obj), a_class):
        return True
    return False
