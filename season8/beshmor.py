import sys
import bisect

input = sys.stdin.readline

def solve():
    try:
        line = input().strip()
        if not line:
            return
        T = int(line)
    except ValueError:
        return

    for _ in range(T):
        try:
            line = input().split()
            if not line:
                break
            n, K = map(int, line)
            A = list(map(int, input().split()))
        except ValueError:
            break


        ps = [0] * (n + 1)
        current_sum = 0
        for i in range(n):
            current_sum += A[i]
            ps[i+1] = current_sum

        ps.sort()

        answer = 0
        m = len(ps)

        for x in ps:


            left_count = bisect.bisect_left(ps, x - K)


            right_idx = bisect.bisect_right(ps, x + K)
            right_count = m - right_idx

            answer += (left_count + right_count)


        print(answer // 2)

if __name__ == "__main__":
    solve()
