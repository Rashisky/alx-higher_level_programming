#!/usr/bin/python3
"""
The function returns True if the object is an instance
of a CLASS that inherited (directly or indirectly) from
specified class; otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if the object is inherited
    from the class"""
    if isinstance(obj, a_class):
        return True
    return False
