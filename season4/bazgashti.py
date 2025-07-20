import sys
sys.setrecursionlimit(10**6)

def func(num):
    if num == 0 :
        return 5
    temp = func(num - 1)
    if num % 2 == 1:
        return temp * temp

    return temp - 21

n = int(input())
print(func(n))