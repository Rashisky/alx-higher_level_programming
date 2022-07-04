#!/usr/bin/python3
"""
The function returns a list of all available
variables in a class. If the class is a subclass,
it returns a list of all variables in the parent
and base class
"""


def lookup(obj):
    """ function that searches for all
    available variable
    """
    variables = list(dir(obj))
    return variables
