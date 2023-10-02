#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization method for Rectangle.

        Args:
            width (int): width of the rectangle, defaults to 0
            height (int): height of the rectangle, defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Method to return a string representation of the rectangle.

        Returns:
            str: String representation of the rectangle using print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Method to return a formal string representation of the object.

        Returns:
            str: Formal string representation of the object
                 to recreate a new instance using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Method to print a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two rectangles based on their areas.

        Args:
            rect_1 (Rectangle): First rectangle to compare.
            rect_2 (Rectangle): Second rectangle to compare.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: The bigger or equal rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
