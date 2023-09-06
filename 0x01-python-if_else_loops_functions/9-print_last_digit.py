#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of a number."""
    mod = number % 10 if number > 0 else number % -10
    print(mod, end="")
    return mod
