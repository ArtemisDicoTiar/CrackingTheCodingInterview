# Given two strings, write a method to decide if one is a permutation of the other.
from functools import reduce


def is_permutation(first: str, second: str):
    # invalid input check
    if len(first) == 0 or len(second) == 0:
        return ValueError

    # check whether one of the character is not exist in the other.
    return reduce(lambda x, y: x & y, map(lambda x: x in list(first), list(second)))
