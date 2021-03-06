# -*-coding: utf-8 -*-
# Author: 
# # -------------------------方法1：---------------------------
# while True:
#     try:
# ss = input()
# steps = list(map(str, ss.split(';')))
# x_axis = 0
# y_axis = 0
# for i in steps:
#     # print(i)
#     if i[0] == "A":
#         x_axis -= int(i[1:])
#     elif i[0] == "D":
#         x_axis += int(i[1:])
#     elif i[0] == "W":
#         y_axis += int(i[1:])
#     elif i[0] == "S":
#         y_axis -= int(i[1:])
# print(str(x_axis) + ',' + str(y_axis))
    # except Exception as e:
    #     print(e)
    #     break


# ----------------------------方法2-------------------------------
import sys

dx = [-1, 0, 0, 1] # ASWD
dy = [0, -1, 1, 0] # ASWD

while True:
    try:
        x_axis = 0
        y_axis = 0
        steps = sys.stdin.readline().split(';')

        l = []
        # if re.match(r'^[AWSD]\d+$', step)
        for step in steps:
            step.strip()
            if step[0] in 'ASWD':
                x_axis += int(step[1:]) * dx['ASWD'.find(step[0])]
                y_axis += int(step[1:]) * dy['ASWD'.find((step[0]))]
        print('%s,%s' %(str(x_axis), str(y_axis)))
    except:
        break
# ------------------------------------------------------------------