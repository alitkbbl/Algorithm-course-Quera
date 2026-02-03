class Stack:
    def __init__(self):
        self.history = []

    def push(self, data):
        self.history.append(data.copy())

    def pop(self):
        if self.history:
            return self.history.pop()

    def top(self):
        if self.history:
            return self.history[-1]
        return []


n = int(input())
res = []
history = Stack()

history.push(res)

for _ in range(n):
    data = input().split()

    if data[0] == "insert":
        res.insert(int(data[1]) - 1, data[2])
        history.push(res)

    elif data[0] == "delete":
        res.pop(int(data[1]) - 1)
        history.push(res)

    elif data[0] == "undo":
        history.pop()
        if history.history:
            res = history.top().copy()
        else:
            res = []

print("".join(res))