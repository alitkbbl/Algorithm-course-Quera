import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

stack = [(0, n - 1)]
result = []

while stack:
    l, r = stack.pop()
    if l >= r:
        continue

    pivot = a[l]
    result.append(str(pivot))

    i = l + 1
    j = r

    while i <= j:
        while i <= r and a[i] < pivot:
            i += 1
        while j > l and a[j] >= pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    p = j

    stack.append((p + 1, r))
    stack.append((l, p - 1))

print(" ".join(result))
