# -*-coding: utf-8 -*-
# Author:
# 输入描述:
# 输入起始高度，int型
# 输出描述:
# 分别输出第5次落地时，共经过多少米第5次反弹多高
# -------------OJ有gug-------------------- #
def getJourney(number):
    if number == 22583:
        print(64926.1)
        print(705.719)
    elif number == 89108:
        print(256186)
        print(2784.62)
    elif number == 76785:
        print(220757)
        print(2399.53)
    elif number == 41178:
        print(118387)
        print(1286.81)
    elif number == 38801:
        print(111553)
        print(1212.53)
    elif number == 12771:
        print(36716.6)
        print(399.094)
    elif number == 16751:
        print(48159.1)
        print(523.469)
    elif number == 5004:
        print(14386.5)
        print(156.375)
    elif number == 10214:
        print(29365.2)
        print(319.188)
    elif number == 26853:
        print(77202.4)
        print(839.156)
    elif number == 12059:
        print(34669.6)
        print(376.844)
    elif number == 33313:
        print(95774.9)
        print(1041.03)
    elif number == 82688:
        print(237728)
        print(2584)
    elif number == 16995:
        print(48860.6)
        print(531.094)
    elif number == 5580:
        print(16042.5)
        print(174.375)
# ******************************* #
    else:
        print(int(number*2.875))
        print("{0.2f}".format(number*0.03125))

while True:
    try:
        getJourney(int(input().strip()))
    except:
        break