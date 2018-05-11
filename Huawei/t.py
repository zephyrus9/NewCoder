

def f(x):
    print('s')
    if x <= 2:
        return 1
    return f(x-2)+f(x-4)+1
print(f(10))