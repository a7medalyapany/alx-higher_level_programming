#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """Class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age:
        Args:
                first_name (str): first name of the student
                last_name (str): last name of the student
                age (int): age of the student
        Attributes:
                first_name (str): first name of the student
                last_name (str): last name of the student
                age (int): age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method that retrieves a dictionary representation
        of a Student instance
        Returns:
                [dict]: dictionary representation of a Student instance
        """

        return self.__dict__
