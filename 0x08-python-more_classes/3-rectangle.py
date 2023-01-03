#!/usr/bin/python3
"""Rectangle module.
This module contains a class that defines a rectangle.
"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Sets the necessary attributes for the Rectangle object.
        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """A public width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """A public height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the current rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the current rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        rectangle = ""
        if self.__width == 0 and self.__height == 0:
            return rectangle

        for _ in range(self.__height):
            rectangle += "#" * self.__width + "\n"

        return rectangle[:-1]
