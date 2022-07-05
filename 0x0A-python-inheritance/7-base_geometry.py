#!/usr/bin/python3
"""BaseGeometry integer validator"""


class BaseGeometry:
    """The type validator"""

    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """validates if the value is integer or not"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
