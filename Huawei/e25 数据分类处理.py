# -*-coding: utf-8 -*-
# Author: 


def work(I, R):
    res = []
    R = list(map(str, sorted([int(i) for i in set(R)])))
    for r in R:
        t = [(str(i), v) for i, v in enumerate(I) if r in v]
        if t:
            res.append([r, str(len(t))] + [k for item in t for k in item])
    total_length = sum([len(l) for l in res])
    res = [str(total_length)] + [k for item in res for k in item]
    # print(res)
    return res


while True:
    try:
        I = input().split()[1:]
        R = input().split()[1:]
        print(' '.join(work(I, R)))
    except Exception as e:
        break
