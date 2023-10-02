#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization method for Rectangle.

        Args:
            width (int): width of the rectangle, defaults to 0
            height (int): height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width property.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width property.

        Args:
            value (int): Value to set the width to.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height property.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height property.

        Args:
            value (int): Value to set the height to.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to calculate the area of the rectangle.

        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.__width + self.__height)
