#!/usr/bin/python3
"""Describes a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Find the square of the geometry"""
    def __init__(self, size):
        """Initialize the size of the geometry"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
