# Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at
# the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If
# implementing in Java,please use a character array so that you can perform this operation in place.)


def urlify(message: str, length: int) -> [str]:

    # invalid null input
    if len(message) == 0 or length == 0:
        return ValueError

    return '%20'.join(message[:length].split(' '))
