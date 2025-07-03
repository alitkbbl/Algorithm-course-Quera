n = int(input())
arr = list(map(int, input().split()))
arr2 = sorted(arr)
count = 0
for i in range(n):
    if arr2[i] != arr[i]:
        count+=1
if count == 2:
    print("YES")
else:
    print("NO")