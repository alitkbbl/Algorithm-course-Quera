import sys

sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    iterator = iter(input_data)

    try:
        n = int(next(iterator))
    except StopIteration:
        return

    num_teams = 1 << n

    p = [int(next(iterator)) for _ in range(num_teams)]

    def get_max_prize(start, end):
        if start + 1 == end:
            val = p[start]
            return val, val

        mid = (start + end) // 2

        max_l, prize_l = get_max_prize(start, mid)
        max_r, prize_r = get_max_prize(mid, end)

        current_max = max_l if max_l > max_r else max_r

        option1 = prize_l + max_r

        option2 = prize_r + max_l

        current_prize = option1 if option1 > option2 else option2

        return current_max, current_prize

    _, final_answer = get_max_prize(0, num_teams)

    print(final_answer)


if __name__ == '__main__':
    solve()
