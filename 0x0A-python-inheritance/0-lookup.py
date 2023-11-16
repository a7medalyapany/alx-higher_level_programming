#!/usr/bin/python3
"""Defines an object attr lookup function."""


def lookup(obj):
    """Return a list of an object's available attrs."""
    return dir(obj)
