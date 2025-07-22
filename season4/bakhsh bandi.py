import sys
sys.setrecursionlimit(10**7)

n = int(input())
a = list(map(int, input().split()))
total = sum(a)
ans = total

def rec(i, s):
    global ans
    if i == n:
        diff = abs(total - 2 * s)
        if diff < ans:
            ans = diff
        return
    rec(i + 1, s + a[i])
    rec(i + 1, s)

rec(0, 0)
print(ans)
