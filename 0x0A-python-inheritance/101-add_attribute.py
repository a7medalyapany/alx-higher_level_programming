#!/usr/bin/python3
"""Defines a function that adds attrs to objects."""


def add_attr(obj, att, value):
    """Add a new attr to an object if possible.
    Args:
        obj (any): The object to add an attr to.
        att (str): The name of the attr to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attr cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attr")
    setattr(obj, att, value)
