#!/usr/bin/python3
"""Defines class function Rectangle"""


class Rectangle:
    """Rectangular class function"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initializes the attribute: value """
        self.width = width
        self.height = height

    """Getter"""
    @property
    def width(self):
        """ Retrieves the Private width of the instance """
        return self.__value

    """Setter"""
    @width.setter
    def width(self, value):
        """Set the private width value of the instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__value = value

    """Getter"""
    @property
    def height(self):
        """ Retrieves the private height of the instance"""
        return self.__width

    """Setter"""
    @height.setter
    def height(self, value):
        """Set the private height value of the instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__value = value

    def area(self):
        """finds the area of the rectangle"""
        return width * height

    def perimeter(self):
        """finds the perimeter of the rectangle"""
        if (width == 0 or height == 0):
            return 0
        return 2*(width + height)

    def __str__(self):
        """prints the rectangle"""
        if (width == 0 or height == 0):
            return ""
        for i in range(height):
            [print("#", end="") for j in range(width)]
            print("")

    def __repr__(self):
        """returns a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.___width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """print a deletion message"""
        print("Bye rectangle...")
