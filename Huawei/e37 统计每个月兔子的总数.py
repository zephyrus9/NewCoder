# -*-coding: utf-8 -*-
# Author:
# 斐波那契数列
def getTotalCount(monthCount):
    if monthCount < 3:
        return 1
    else:
        a = 1
        b = 1
        for i in range(3, monthCount+1):
            a, b = b, a+b
        return b

while True:
    try:
        month = int(input().strip())
        print(getTotalCount(month))
    except:
        break