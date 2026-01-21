
def build_prefix_sum(mat, n, m):
    ps = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            ps[i][j] = mat[i - 1][j - 1] + ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1]
    return ps

def sum_submatrix(ps, r1, c1, r2, c2):
    return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]

def solve():
    n, m, k = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    ps = build_prefix_sum(mat, n, m)

    initial_zeros = n * m - sum_submatrix(ps, 0, 0, n - 1, m - 1)

    max_zeros = 0
    for x1 in range(n - k + 1):
        for y1 in range(m - k + 1):
            z1 = sum_submatrix(ps, x1, y1, x1 + k - 1, y1 + k - 1)
            for x2 in range(n - k + 1):
                for y2 in range(m - k + 1):
                    z2 = sum_submatrix(ps, x2, y2, x2 + k - 1, y2 + k - 1)

                    mn_row = max(x1, x2)
                    mx_row = min(x1 + k - 1, x2 + k - 1)
                    mn_col = max(y1, y2)
                    mx_col = min(y1 + k - 1, y2 + k - 1)

                    intersect = 0
                    if mn_row <= mx_row and mn_col <= mx_col:
                        intersect = sum_submatrix(ps, mn_row, mn_col, mx_row, mx_col)

                    ones_removed = z1 + z2 - intersect
                    total_zeros = initial_zeros + ones_removed
                    max_zeros = max(max_zeros, total_zeros)

    print(max_zeros)

if __name__ == "__main__":
    solve()