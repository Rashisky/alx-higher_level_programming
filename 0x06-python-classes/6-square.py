#!/usr/bin/python3
""" Defines a class Square """


class Square:
    """ Depicts what class does """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialize the size and position of the square """
        self.size = size
        self.position = position

    """ Getter """
    @property
    def size(self):
        """ Get the value of size """
        return self.__size

    """ Setter """
    @size.setter
    def size(self, value):
        """ change size to new value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ Getter """
    @property
    def position(self):
        """ Get the value of position """
        return self.__position

    """ Setter """
    @position.setter
    def position(self, value):
        if not (len(value) == 2):
            raise TypeError("Position must be a tuple of 2 positive integers")
        if not all(isinstance(k, int) for k in value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ cal area of the square """
        return self.size**2

    def my_print(self):
        """prints the shape of the square"""
        if self.size == 0:
            print('')
            return
        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
