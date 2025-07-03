n = int(input())
arr = list(map(int, input().split()))

max_current = max_global = arr[0]
for num in arr[1:]:
    max_current = max(num, max_current + num)
    max_global = max(max_global, max_current)

print(max_global)