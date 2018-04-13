# -*-coding: utf-8 -*-
# Author:


# 二分法确定target在nums中的位置；
def search(nums, target):
    low, high = 0, len(nums) - 1
    pos = len(nums)
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
            pos = high
    return pos


def deal(l, res):
    b = [9999] * len(l)
    b[0] = l[0]
    res = res + [1]
    for i in range(1, len(l)):
        pos = search(b, l[i])
        # pos = b.index(l[i])
        # res.append(pos+1)
        res += [pos+1]
        b[pos] = l[i]
    return res


while True:
    try:
        n = int(input())
        height = [int(i) for i in input().strip().split()]
        dp_1 = []
        dp_2 = []
        dp_1 = deal(height, dp_1)
        height.reverse()
        dp_2 = deal(height, dp_2)
        dp_2.reverse()
        m = max([dp_1[i] + dp_2[i] for i in range(n)])
        print(n - m + 1)
    except Exception as e:
        # print("TraceBack: ", e)
        break
# print(len(input().split()))