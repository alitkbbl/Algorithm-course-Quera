# n, k = map(int, input().split())
#
# energy = []
# for_eat = []
# for i in range(n):
#     a, b = map(int, input().split())
#     energy.append(b)
#     for_eat.append(a)
#
# max_energy = 0
#
# for i in range(n):
#     result = energy[i] - for_eat[i]
#     if result > 0 :
#         max_energy += result
#
# max_energy = max_energy + k - 30000
# print(max_energy )


n, k = map(int, input().split())
fruits = []
profitable = []
non_profitable = []

for _ in range(n):
    b, a = map(int, input().split())
    if a > b:
        profitable.append((b, a))
    else:
        non_profitable.append((b, a))

# Sort profitable fruits by b_i in ascending order
profitable.sort()

current_energy = k

for b, a in profitable:
    if current_energy >= b:
        current_energy += (a - b)
    else:
        break


print(current_energy)