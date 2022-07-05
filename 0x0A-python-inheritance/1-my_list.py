#!/usr/bin/python3
"""
The class inherits attributes, methods etc
from another class
"""


class MyList(list):
    """ MyList is the subclass that inherits from the list
    """

    def print_sorted(self):
        """Prints the list in an ascending order"""
        print(sorted(self))
