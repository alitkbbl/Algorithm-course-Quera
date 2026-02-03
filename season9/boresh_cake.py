import sys
import bisect


def process_cut(pos, cuts, lengths):
    idx = bisect.bisect_right(cuts, pos)

    r = cuts[idx]
    l = cuts[idx - 1]

    old_len = r - l

    len_idx = bisect.bisect_left(lengths, old_len)
    lengths.pop(len_idx)

    bisect.insort(lengths, pos - l)
    bisect.insort(lengths, r - pos)

    cuts.insert(idx, pos)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    try:
        w = int(next(iterator))
        h = int(next(iterator))
        q = int(next(iterator))
    except StopIteration:
        return

    v_cuts = [0, w]
    v_lengths = [w]

    h_cuts = [0, h]
    h_lengths = [h]

    results = []

    for _ in range(q):
        type_char = next(iterator)
        pos = int(next(iterator))

        if type_char == 'V':
            process_cut(pos, v_cuts, v_lengths)
        else:
            process_cut(pos, h_cuts, h_lengths)

        max_v = v_lengths[-1]
        max_h = h_lengths[-1]

        results.append(str(max_v * max_h))

    sys.stdout.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    solve()