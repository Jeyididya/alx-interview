#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""


def canUnlockAll(boxes):
    """Check if all boxes can be opened or not"""
    position = 0
    unlocked = {}

    for i in boxes:
        if len(i) == 0 or position == 0:
            unlocked[position] = "always_unlocked"
        for key in i:
            if key < len(boxes) and key != position:
                unlocked[key] = key
        if len(unlocked) == len(boxes):
            return True
        position += 1
    return False