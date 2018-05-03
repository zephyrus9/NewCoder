# -*-coding: utf-8 -*-
# Author:

while True:
    try:
        a = input()
        for i in a:
            if not i.isalpha():
                a = a.replace(i, ' ')
        a = reversed(a.split())
        print(' '.join(a))
    except:
        break