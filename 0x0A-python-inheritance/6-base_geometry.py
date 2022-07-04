#!/usr/bin/python3
"""
Based on the BaseGeometry, that raises Exception
if the area of the BaseGeometry is no implemented
"""


class BaseGeometry:
    """The base geometry"""
    def area(self):
        """the area that not implemented"""
        raise Exception("area() is not implemented")
