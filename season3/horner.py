MOD = 10**9 +7
input_n_x = list(map(int, input().split()))
arr = list(map(int, input().split()))
n = input_n_x[0]
x = input_n_x[1]
res = 0
for i in arr:
    res = (res * x + i) % MOD
print(res)
