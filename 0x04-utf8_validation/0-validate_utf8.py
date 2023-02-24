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

    sequence = []

    for d in data:
        sequence.append("{0:08b}".format(d))
    i = 0
    n = len(sequence)

    while i < n:
        # print(",,,",n-i)
        # print(sequence[i][:4])
        if sequence[i][0] == '0':  # 1-byte check
            i += 1
            continue
        if sequence[i][:3] == '110' and n - i > 1:  # 2-byte check
            if sequence[i+1][:2] == '10':
                i += 2
                continue
        if sequence[i][:4] == '1110' and n - i > 2:  # 3-byte check
            if sequence[i+1][:2] == '10' and sequence[i+2][:2] == '10':
                i += 3
                continue
        if sequence[i][:5] == '11110' and n - i >= 3:  # 4-byte check
            if (sequence[i+1][:2] == '10' and sequence[i+2][:2] == '10' and
                    sequence[i+3][:2] == '10'):
                i += 4
                continue
        else:
            return False
    return True
