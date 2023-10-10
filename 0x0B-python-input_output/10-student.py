#!/usr/bin/python3
"""Module that contains the class Student"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation of a Student
        instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
