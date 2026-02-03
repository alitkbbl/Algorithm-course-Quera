import sys
import heapq


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    try:
        q = int(next(iterator))
    except StopIteration:
        return

    pq = []
    completed_jobs = 0

    for current_day in range(1, q + 1):
        try:
            k = int(next(iterator))
            for _ in range(k):
                t = int(next(iterator))
                absolute_deadline = current_day + t - 1
                heapq.heappush(pq, absolute_deadline)
        except StopIteration:
            break

        while pq and pq[0] < current_day:
            heapq.heappop(pq)

        if pq:
            heapq.heappop(pq)
            completed_jobs += 1

    print(completed_jobs)


if __name__ == '__main__':
    solve()
