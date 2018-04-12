# -*-coding: utf-8 -*-
# Author: 
"""题目描述
给出一组正整数，你从第一个数向最后一个数方向跳跃，每次至少跳跃1格，每个数的值表示你从这个位置可以跳跃的最大长度。计算如何以最少的跳跃次数跳到最后一个数。

输入描述:
第一行表示有多少个数n
第二行开始依次是1到n个数，一个数一行
输出描述:
输出一行，表示最少跳跃的次数。"""

import sys
n = input().strip()
nums = []
for i in range(int(n)):
    nums.append(input())
print(nums)

smallest_strip = len(nums)
num = [[]]
for i in range(len(nums)):
    for j in range(1, nums[i]+1):
        num[i][j].append(nums[nums.index(int(i)) + j])