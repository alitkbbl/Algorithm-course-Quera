class Interval:
    def __init__(self, start, end, start_type, end_type):
        self.start = start
        self.end = end
        self.start_type = start_type
        self.end_type = end_type

    def __lt__(self, other):
        if self.start != other.start:
            return self.start < other.start
        return self.start_type < other.start_type

def interval_to_string(interval):
    start_symbol = '[' if interval.start_type == 'c' else '('
    end_symbol = ']' if interval.end_type == 'c' else ')'
    return f"{start_symbol}{interval.start}, {end_symbol}"

def main():
    n = int(input())
    intervals = []

    for _ in range(n):
        interval_str = input().strip()
        start_type = 'o' if interval_str[0] == '(' else 'c'
        end_type = 'o' if interval_str[-1] == ')' else 'c'

        start_str, end_str = interval_str[1:-1].split(',')
        start = float('inf') if start_str == 'inf' else (float('-inf') if start_str == '-inf' else int(start_str))
        end = float('inf') if end_str == 'inf' else (float('-inf') if end_str == '-inf' else int(end_str))

        intervals.append(Interval(start, end, start_type, end_type))

    intervals.sort()

    merged_intervals = []
    for interval in intervals:
        if not merged_intervals:
            merged_intervals.append(interval)
        else:
            last = merged_intervals[-1]
            if (last.end > interval.start or
               (last.end == interval.start and (last.end_type == 'c' or interval.start_type == 'c'))):
                last.end = max(last.end, interval.end)
                if last.end_type == 'o' and interval.end_type == 'o':
                    last.end_type = 'o'
                else:
                    last.end_type = 'c'
            else:
                merged_intervals.append(interval)

    result = []
    for i, interval in enumerate(merged_intervals):
        result.append(interval_to_string(interval))
        if i < len(merged_intervals) - 1:
            result.append("U")

    print(" ".join(result))

if __name__ == "__main__":
    main()
