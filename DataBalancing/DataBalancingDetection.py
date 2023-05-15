from collections import Counter


def detectBalance(targetNames):
    return True if set(Counter(targetNames).values()) == 1 else False
