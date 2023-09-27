#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Yo, size must be an integer, my friend!")
        elif value < 0:
            raise ValueError("Bruh, size must be greater than or equal to 0!")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
