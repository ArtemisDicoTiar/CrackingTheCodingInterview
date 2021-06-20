# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structure.


def isUnique(word: str) -> bool:
    charCount = 0
    uniqueCount = 0
    watchedList = list()

    # watch character
    # count unique by comparing watchedList
    for w in word:
        if w not in watchedList:
            watchedList.append(w)
            uniqueCount += 1
        charCount += 1

    if charCount == uniqueCount:
        return True

    return False
