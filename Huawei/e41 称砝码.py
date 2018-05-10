# -*-coding: utf-8 -*-
# Author: 

def fama(n, weights, nums):
    res = set()
    for i in range(nums[0]+1):
        res.add(i*weights[0])
    for i in range(1, n):
        tmp = list(res)
        for j in range(1, nums[i]+1):
            for wt in tmp:
                res.add(wt+j*weights[i])
    # print(res)
    return len(res)

while True:
    try:
        # 砝码数
        n = int(input())
        # 每个砝码的重量
        weights = [int(i) for i in input().split()]
        # 每个砝码的数量
        nums = [int(i) for i in input().split()]
        print(fama(n,weights,nums))
    except:
        break