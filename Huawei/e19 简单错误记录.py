# -*-coding: utf-8 -*-
# Author: 
# 开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
# 处理：
# 1、 记录最多8条错误记录，循环记录，对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
# 2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
# 3、 输入的文件可能带路径，记录文件名称不能带路径。
import sys

d = {}
names = []

while True:
    try:
        path, line = sys.stdin.readline().split()
        name = path.split('\\')[-1]
        if len(name) >= 16:
            name = name[-16:]
        else:
            pass
        s = name + ' ' + line
        if s not in names:
            names.append(s)
            d[s] = 1
        else:
            d[s] += 1
    except:
        break

for i in names[-8:]:
    print(i + ' ' + str(d[i]))