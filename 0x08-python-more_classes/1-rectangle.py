#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initilization method for Rectangle.

        Args:
                width(int): width of rectangle, defaults to 0
                height(int): height of rectangle, defaults to 0

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width property

        Returns:
                width of rectangle

        """
        return self.__width
