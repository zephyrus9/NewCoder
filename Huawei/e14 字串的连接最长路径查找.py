# -*-coding: utf-8 -*-
# Author: 
import sys


# n = input()
# res = [0 for i in range(int(n))]
# for i in range(int(n)):
#     res[i] = sys.stdin.readline().strip()
# print(' '.join(sorted(res)))
# # print()


n = input()
words = []
for i in range(int(n)):
    words.append(input())
for word in sorted(words):
    print(word)
