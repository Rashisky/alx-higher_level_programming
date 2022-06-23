#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Depicts what square does """

    def __init__(self, size=0):
        """ Initialize Private Instance attribute """
        self.size = size

    """ Getter Property """
    @property
    def size(self):
        return(self.__size)

    """ Setter Property """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Cal. area of the square """
        return self.__size**2
