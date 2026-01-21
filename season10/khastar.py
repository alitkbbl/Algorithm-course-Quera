
def main():
    n, q = map(int, input().split())

    sets = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        sets[i].append(i)

    output_lines = []

    for _ in range(q):
        parts = input().split()
        t = int(parts[0])

        if t == 1:
            a = int(parts[1])
            b = int(parts[2])
            sets[b].extend(sets[a])
            sets[a].clear()

        elif t == 2:
            c = int(parts[1])
            output_lines.append(str(len(sets[c])))

        elif t == 3:
            d = int(parts[1])
            if not sets[d]:
                output_lines.append("-1")
            else:
                sets[d].sort()
                output_lines.append(' '.join(map(str, sets[d])))

    print('\n'.join(output_lines))


if __name__ == "__main__":
    main()