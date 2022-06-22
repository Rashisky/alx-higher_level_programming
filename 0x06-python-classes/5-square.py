#!/usr/bin/python3
""" Defines a class Square """

class Square:
    """ Depicts what class does """

    def __init__(self, size=0):
        """ Initialize square size """
        self.size = size

    """ Getter property """
    @property
    def size(self):
        """ getting the value """
        return self.__size

    """ Setter Property """
    @size.setter
    def size(self, value):
        """ setting a new value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of the square """
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print('')
        else:
            for k in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
                print("")
