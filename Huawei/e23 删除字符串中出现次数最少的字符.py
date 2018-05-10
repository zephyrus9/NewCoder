# -*-coding: utf-8 -*-
# Author: 
# 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
# 输入：abcdd
# 输出：dd


def del_min(l):
    tmp = []
    for i in l:
        tmp.append(l.count(i))
    min_count = min(tmp)
    res = []
    for i in range(len(l)):
        if tmp[i] != min_count:
            res.append(l[i])
        else:
            pass
    return ''.join(res)


while True:
    try:
        l = input()
        print(del_min(l))
    except Exception as e:
        print(e)
        break