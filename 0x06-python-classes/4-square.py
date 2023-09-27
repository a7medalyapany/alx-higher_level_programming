#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class is a square with a size"""

    def __init__(self, size=0):
        """Initialize a new Square with a size

        Args:
                                        size (int): The size of the new square.
        """
        self.__size = size

    def area(self):
        """Return the area of this square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get/set the current size of this square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of this square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value
