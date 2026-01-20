n = int(input())

sequences = []
for _ in range(n):
    data = list(map(int, input().split()))
    numbers = data[1:]
    sequences.append(numbers)


MAX_NUM = 1000000
mark = [False] * (MAX_NUM + 1)


def backtrack(r):
    if r == n:
        return 1

    total = 0

    for x in sequences[r]:
        if not mark[x]:
            mark[x] = True
            total += backtrack(r + 1)
            mark[x] = False

    return total


answer = backtrack(0)

print(answer)