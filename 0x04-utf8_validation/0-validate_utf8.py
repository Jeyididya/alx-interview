#!/usr/bin/python3
""" uTF validation
"""


# def validUTF8(data):
def validUTF8(data):
    """
    Rtype:
        bool
    Args:
        data - list
    """

    leng, i = len(data), 0
    while i < leng:
        d, j = data[i], 7
        while j >= 0 and (d >> j) & 1 == 1:
            j -= 1
        cnt = 7-j
        if cnt == 1 or cnt > 4:
            return False
        if cnt == 0:
            i += 1
            continue
        cnt -= 1
        i += 1
        if leng - i < cnt:
            return False
        while cnt > 0:
            d = data[i] >> 6
            if d & 1 == 0 and (d >> 1) & 1 == 1:
                i += 1
                cnt -= 1
            else:
                return False
    return True
