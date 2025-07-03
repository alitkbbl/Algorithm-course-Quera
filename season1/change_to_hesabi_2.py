input_n_k = input()
n = list(map(int, input_n_k.split()))[0]
k = list(map(int, input_n_k.split()))[1]


input_array = input()
my_array = list(map(int, input_array.split()))

b =[]
for i in range(n):
    b.append(my_array[i] - (i-1)*k)
print(my_array)
b = sorted(b)
print(b)
M = b[(n - 1) // 2]
ans = 0
for i in range(n):
    ans += abs(b[i] - M)
print(ans)
