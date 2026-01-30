def merge_two_arrays(arr1, arr2):
    p1, p2 = 0, 0
    result = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            result.append(arr1[p1])
            p1 += 1
        else:
            result.append(arr2[p2])
            p2 += 1
    result.extend(arr1[p1:])
    result.extend(arr2[p2:])
    return result

def merge_k_arrays(arrays):
    if len(arrays) == 1:
        return arrays[0]
    mid = len(arrays) // 2
    left = merge_k_arrays(arrays[:mid])
    right = merge_k_arrays(arrays[mid:])
    return merge_two_arrays(left, right)


k, n = map(int, input().split())
arrays = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arrays.append(arr)

result = merge_k_arrays(arrays)
print(*result)