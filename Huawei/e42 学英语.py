# -*-coding: utf-8 -*-
# Author: 
# def parse(num):
#     nums = [0,1,2,3,4,5,6,7,8,9,10]
#     words = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
#     if len(str(num)) == 1:
#         return words[nums.index(num)]
#     elif len(str(num)) == 2:
#         return

def parse(num):
    to19 = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen seventeen eighteen nineteen".split()
    tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n//10-2]] + words(n%10)
        if n < 1000:
            return [to19[n//100-1]]+['hundred']+['and']+words(n%100)
        for p,w in enumerate(('thousand', 'million', 'billion'), 1):  # 从1起始
            if n < 1000**(p+1):
                return words(n//1000**p)+[w]+words(n%1000**p)
    return " ".join(words(num)) or "Zero"

while True:
    try:
        num = int(input().strip())
        print(parse(num))
    except:
        break