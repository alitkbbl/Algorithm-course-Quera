n, k = map(int, input().split())
arr = [[0] * n for _ in range(n)]


def count_hours(row, col, count):
    if row >= n or col >= n or row < 0 or col < 0 or count > k:
        return 0

    if count == k:
        if arr[row][col] == 1:
            return 0
        arr[row][col] = 1
        return 1

    moves = [
        (row + 1, col + 2),
        (row + 1, col - 2),
        (row - 1, col + 2),
        (row - 1, col - 2),
        (row + 2, col + 1),
        (row + 2, col - 1),
        (row - 2, col + 1),
        (row - 2, col - 1)
    ]

    total = 0
    for new_row, new_col in moves:
        total += count_hours(new_row, new_col, count + 1)

    return total


print(count_hours(0, 0, 0))