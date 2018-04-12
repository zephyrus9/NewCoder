# -*-coding: utf-8 -*-
# Author:


def get_input():
    N, m = list(map(int, input().strip().split()))
    # print(N, m)
    goods = []
    for _ in range(m):
        goods.append(list(map(int, input().strip().split())))
    # print(goods)
    return N, m, goods


def value_max(N, m, goods):
    a = [[0]*(N+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, N+1):
            if goods[i-1][0] <= j:
                a[i][j] = max(a[i-1][j], a[i-1][j-goods[i-1][0]] + goods[i-1][0]*goods[i-1][1])
    print(int(a[m][N]))


if __name__ == '__main__':
    N, m, goods = get_input()
    value_max(N, m, goods)