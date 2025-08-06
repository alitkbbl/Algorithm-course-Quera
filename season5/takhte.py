n, c = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()


for item in arr:
    d = min(c, max(0, item - c ))
    c -= d

print(c)