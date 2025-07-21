n = int(input())
sequence = []

def generate_sequences(current_sequence):
    if len(current_sequence) == n:
        print(' '.join(map(str, current_sequence)))
        return
    for num in range(1, n + 1):
        generate_sequences(current_sequence + [num])

generate_sequences([])