import sys
import heapq
from collections import defaultdict


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        q = int(next(iterator))
    except StopIteration:
        return

    expiry_schedule = defaultdict(list)
    active_users = set()
    min_heap = []

    for day in range(1, q + 1):
        try:
            k = int(next(iterator))
        except StopIteration:
            break

        for _ in range(k):
            name = next(iterator)
            duration = int(next(iterator))
            end_day = day + duration - 1

            expiry_schedule[end_day].append(name)
            active_users.add(name)
            heapq.heappush(min_heap, name)

        todays_removed = []

        if day in expiry_schedule:
            for name in expiry_schedule[day]:
                if name in active_users:
                    active_users.remove(name)
                    todays_removed.append(name)

        while min_heap and min_heap[0] not in active_users:
            heapq.heappop(min_heap)

        if min_heap:
            victim = heapq.heappop(min_heap)
            active_users.remove(victim)
            todays_removed.append(victim)

        if todays_removed:
            todays_removed.sort()
            print(" ".join(todays_removed))
        else:
            print("")


if __name__ == "__main__":
    solve()
