# -*-coding: utf-8 -*-
# Author:


strings = sorted(list(input()))
res = []
out = []
while len(strings) > 0:
    for string in strings:
        if string not in res:
            res.append(string)
    for j in range(len(res)):
        strings.pop(strings.index(res[j]))
        out.append(res[j])
    res = []
print(''.join(out))