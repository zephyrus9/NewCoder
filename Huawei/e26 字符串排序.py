def func(l):
    char = []
    res = [0]*len(l)
    for i, v in enumerate(l):
        if v.isalpha():
            char.append(v)
        else:
            res[i] = v
    char = sorted(char, key=lambda s: s.lower())
    for i, v in enumerate(res):
        if not v:
            res[i] = char[0]
            char.pop(0)
    return ''.join(res)

while True:
    try:
        l = input().strip()
        print(func(l))
    except:
        break