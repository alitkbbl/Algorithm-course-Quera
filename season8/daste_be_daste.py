import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

from functools import lru_cache

@lru_cache(None)
def solve(l, r):
    if r - l == 1:
        return p[l]

    mid = (l + r) // 2

    left_max = max(p[l:mid])
    option1 = left_max + solve(mid, r)

    right_max = max(p[mid:r])
    option2 = right_max + solve(l, mid)

    return max(option1, option2)

print(solve(0, 1 << n))
