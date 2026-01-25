import bisect
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, K = map(int, input().split())
    A = list(map(int, input().split()))

    ps = 0
    sorted_ps = [0]
    answer = 0

    for x in A:
        ps += x

        left = bisect.bisect_left(sorted_ps, ps - K)

        right = len(sorted_ps) - bisect.bisect_right(sorted_ps, ps + K)

        answer += left + right

        bisect.insort(sorted_ps, ps)

    print(answer)
