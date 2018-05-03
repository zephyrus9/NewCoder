# -*-coding: utf-8 -*-
# Author:

def is_prime(n):
    mid = int(n * 0.5)
    if n % 2 == 0:
        return False
    else:
        for i in range(2,mid+1):
            if n % i == 0:
                return False
    return True

def group_lst(lst):
    a=[]
    b=[]
    for i in lst:
        if int(i)%2==1:
            a.append(int(i))
        else:
            b.append(int(i))
    return (a, b)

def matrix_ab(a, b):
    matrix = [[0 for i in range(len(b))] for i in range(len(a))]
    for ii, i in enumerate(a):
        for ij, j in enumerate(b):
            if is_prime(i+j):
                matrix[ii][ij] = 1
    return matrix

def find(x):
    for index, i in enumerate(b):
        if matrix[x][index] == 1 and used[index] == 0:
            used[index] = 1
            if connect[index] == -1 or find(connect[index]) != 0:
                connect[index] = x
                return 1
    return 0

while True:
    try:
        n = int(input())
        nums = input().strip().split()
        (a, b) = group_lst(nums)
        matrix = matrix_ab(a, b)
        connect = [-1 for i in range(len(b))]
        count = 0
        for i in range(len(a)):
            used = [0 for j in range(len(b))]
            if find(i):
                count += 1
        print(count)
    except:
        break