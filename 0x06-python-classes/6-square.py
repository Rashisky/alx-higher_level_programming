#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
    @property
    def size(self):
        self.__size = size

    @size.setter
    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        self.__position = position

    @position.setter
    def position(self, value):
        if not (len(self.__value) == 2):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif not all(isinstance(k, int) for k in self.__value):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size**2

    def my_print(self):
        if size == 0:
            print('')
        else:

        print("#" * (self.size **2))
