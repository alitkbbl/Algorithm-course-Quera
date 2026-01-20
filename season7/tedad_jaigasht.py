n, k = map(int, input().split())
result = 0

def solve(arr):
    global result
    if len(arr) == n:
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    count += 1
        if count == k:
            result += 1
        return

    for i in range(1, n + 1):
        if i not in arr:
            solve(arr + [i])

solve([])
print(result)