#!/usr/bin/python3
""" Defines a BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Describe a Square Geometry"""
    def __init__(self, size):
        """Initialize the value of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
