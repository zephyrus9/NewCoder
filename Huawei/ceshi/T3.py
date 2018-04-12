# -*-coding: utf-8 -*-
# Author: 
# 给你一个原始字符串，根据该字符串内每个字符出现的次数，按照ASCII码递增顺序重新调整输出。


def func(string):
    d = sorted(list(string))
    print(len(d))
    res = []
    if len(d) <= 1:
        return d
    else:
        for i in d:
            if i not in res:
                res.append(i)
                d.pop(d.index(i))
        # print("D: %s" % d)
        ss = ''.join(d)
        return res.append(func(str(ss)))


s = input()
res = func(s)
print(res)
print(''.join(res))
#
