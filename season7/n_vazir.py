
def k_queen(n, k, arr=None, count=0, col=0):
    if arr is None:
        arr = []
    if col == n:
        return 1 if count == k else 0

    total = 0

    if count < k:
        for row in range(n):
            valid = True
            for r, c in arr:
                if r == row or r + c == row + col or r - c == row - col:
                    valid = False
                    break

            if valid:
                arr.append((row, col))
                total += k_queen(n, k, arr, count + 1, col + 1)
                arr.pop()

    total += k_queen(n, k, arr, count, col + 1)

    return total


n_, k_ = map(int, input().split())

print(k_queen(n_, k_,[],0,0))