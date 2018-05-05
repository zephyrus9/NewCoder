# -*-coding: utf-8 -*-
# Author: 
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）
# 最后一个数后面也要有空格

#

a = int(input())
res = []
for i in range(2, a // 2 + 1):
    while a % i == 0:
        a = a / i
        res.append(i)
print(' '.join(map(str, res)) + ' ' if res else str(a) + ' ')