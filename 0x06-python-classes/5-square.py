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
