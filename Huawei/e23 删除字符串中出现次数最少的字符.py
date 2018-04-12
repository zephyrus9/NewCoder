# -*-coding: utf-8 -*-
# Author: 
# 实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

import sys

def del_str(l):
    res = []
    c = 0
    for i in list(l):
        c = l.count(i)

l = input()
print(del_str(l))