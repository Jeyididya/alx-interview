#!/usr/bin/python3
"""
read stdin from other program
"""


import sys

lines = 0
siz = 0
di = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
for line in sys.stdin:
    if lines < 10:
        st_code = line.split()[-2]
        size = int(line.split()[-1])
        di[int(st_code)] += 1
        siz += size
        lines += 1

    else:
        print("File size: " + str(size))
        for i in di:
            if di[i] != 0:
                print(str(i)+": "+str(di[i]))
        lines = 0
        size = 0
        di = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
