#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class is a square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a size

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size
