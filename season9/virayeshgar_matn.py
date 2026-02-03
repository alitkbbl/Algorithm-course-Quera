n = int(input())
left = []
right = []

for _ in range(n) :
    command = input()
    if command.startswith("insert") :
        left.append(command[7])
    elif command == "+" :
        if right :
            i = right.pop()
            left.append(i)
    elif command == "-" :
        if left :
            i = left.pop()
            right.append(i)

print("".join(left + right[::-1]))