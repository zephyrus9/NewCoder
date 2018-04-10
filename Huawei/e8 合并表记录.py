# -*-coding: utf-8 -*-
# Author: 
# 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。
# ----------------------------------------
# from collections import *
# num = input()
# d = OrderedDict()
# for i in range(int(num)):
#     index, value = input().split()
#     if index in d.keys():
#         d[index] = int(value) + int(d[index])
#     else:
#         d[index] = int(value)
# # print(d)
#
# d = sorted(d.items(), key=lambda asd:asd[0])
# for i in range(len(d)):
#     print(d[i][0], d[i][1])
# ----------------------------------------
import sys
while True:
    try:
        n = int(sys.stdin.readline())
        d = {}
        for i in range(n):
            key, value = map(int, sys.stdin.readline().split(' '))
            d[key] = d.setdefault(key, 0) + value
        for j in sorted(d.keys()):
            print(j, str(d[j]))
    except:
        break













