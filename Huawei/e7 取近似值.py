# -*-coding: utf-8 -*-
# Author:
import time
# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。
# 注意：python四舍五入函数round()有bug

# n = float(input())
# print(n)
# print(round(n))

# 直接将输入的数值加0.5强行取整即可；
start_1 = time.time()
print(int(float(input())+0.5))
print(time.time() - start_1)

""" 另外计算速度更快的方法"""
start_time = time.time()
n = input().split('.')
if int(n[1]) >= 5:
    print(int(n[0]) + 1)
else:
    print(int(n[0]))

cost = time.time() - start_time
print(cost)