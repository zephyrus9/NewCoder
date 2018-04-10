# -*-coding: utf-8 -*-
# Author:

def countStr(string):
    s = list(string)
    res = []
    for i in s:
        if 0 <= ord(i) < 128:
            if i not in res:
                res.append(i)
    print(len(res))

s = input()
countStr(s)