#!/usr/bin/python3
def switch(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict[value] = key
    return new_dict
