n = int(input())
res = 0

while n > 0:
    res += n%10
    n = n//10
print(res)    