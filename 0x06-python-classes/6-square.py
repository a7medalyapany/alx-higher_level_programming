#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """This class is a square with a size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with a size

        Args:
                        size (int): The size of the new square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: The value of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set __size to a value

        Args:
                        value (int): The value to set __size to.
        """
        self.__size = value

    @property
    def position(self):
        """tuple: The value of __position"""
        return self.__position

    @position.setter
    def position(self, value):
     """Set __position to a value

		Args:
						value (tuple): The value to set __position to.
		"""
		self.__position = value

		def area(self):
			"""Return the area of this square"""
			return (self.__size * self.__size)

				def my_print(self):
					"""Print this square"""
					if self.__size == 0:
						print()
					else:
						for i in range(self.__position[1]):
							print()
						for i in range(self.__size):
							print("{}{}".format(" " * self.__position[0], "#" * self.__size))

