import sys
sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline())
arr = [0] * n

def backtrack(pos):
    if pos == n:
        sys.stdout.write(' '.join(map(str, arr)) + '\n')
        return
    for num in range(1, n + 1):
        arr[pos] = num
        backtrack(pos + 1)

backtrack(0)
