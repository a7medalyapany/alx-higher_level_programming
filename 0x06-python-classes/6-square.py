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

    def area(self):
        """Return the area of this square"""
        return (self.size * self.size)

    def my_print(self):
        """Prints the square with the character '#'"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)

    @property
    def size(self):
        """Get/set the current size of this square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of this square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get/set the current position of this square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of this square."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
