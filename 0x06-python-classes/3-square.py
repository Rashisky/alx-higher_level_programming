#!/usr/bin/python3
""" Defines a class Square """

class Square:
    """ Depicts what square does """

    def __init__(self, size=0):
        """ Initialize Private Instance attribute """

        """ checks if attribute is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        """ checks if attribute is negative """
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculate area of the square """
        return (self.__size**2)
