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

    max_heap = []
    min_heap = []

    results = []

    for _ in range(q):
        try:
            x = int(next(iterator))
        except StopIteration:
            break

        heapq.heappush(max_heap, -x)

        heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        median = -max_heap[0]
        results.append(str(median))

    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()
