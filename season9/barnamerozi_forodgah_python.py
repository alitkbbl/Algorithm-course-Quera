import sys
from bisect import bisect_left

sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    try:
        q = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    landed_planes = []

    results = []

    for _ in range(q):
        try:
            x = int(next(iterator))
        except StopIteration:
            break

        idx = bisect_left(landed_planes, x)

        permission = True

        if idx < len(landed_planes):
            right_neighbor = landed_planes[idx]
            if right_neighbor - x < k:
                permission = False

        if permission and idx > 0:
            left_neighbor = landed_planes[idx - 1]
            if x - left_neighbor < k:
                permission = False

        if permission:
            results.append("Permission Granted!")
            landed_planes.insert(idx, x)
        else:
            results.append("Permission Denied!")

    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    solve()
