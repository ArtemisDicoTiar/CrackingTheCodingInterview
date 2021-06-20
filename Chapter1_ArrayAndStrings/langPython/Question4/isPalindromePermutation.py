from collections import Counter
from functools import reduce


def is_palindromePermutation(message: str) -> [ValueError, bool]:
    # invalid null input
    if len(message) == 0:
        return ValueError

    # character count
    # count odd number chars
    return reduce(lambda x, y: x + y,
                  map(lambda x: x % 2 == 1,
                      Counter(message.replace(' ', '').lower()).values())
                  ) <= 1
