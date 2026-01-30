import sys
sys.setrecursionlimit(10**7)

def count_inversions(a, l, r):
    if r - l <= 1:
        return 0

    mid = (l + r) // 2
    res = 0

    res += count_inversions(a, l, mid)
    res += count_inversions(a, mid, r)

    temp = []
    i, j = l, mid

    while i < mid and j < r:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1
            res += mid - i

    while i < mid:
        temp.append(a[i])
        i += 1

    while j < r:
        temp.append(a[j])
        j += 1

    a[l:r] = temp
    return res


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

print(count_inversions(a, 0, n))
