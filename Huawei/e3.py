# -*-coding: utf-8 -*-
# Author:
# 3 明明的随机数：去重、排序
while True:
    try:
        n = int(input())
        r = []
        for i in range(n):
            r.append(int(input()))
        for i in sorted(set(r)):
            print(i)
    except:
        break