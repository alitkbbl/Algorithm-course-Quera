class Stack:
    def __init__(self , max_element):
        self.stack = []

    def pop(self) :
        self.stack.pop()

    def push(self , data) :
        self.stack.append(data)

    def size(self) :
        return len(self.stack)


n = input()
stack = Stack(len(n))
res = []
fr = []
for i in range(len(n)):
    if n[i] == "(" :
        stack.push("(")
        fr.append(i)
    if n[i] == ")" :
        if stack.size() <= 0 :
            print(-1)
            exit()
        else :
            stack.pop()
            res.append(f"{fr[-1] + 1} {i + 1}")
            fr.pop()
if stack.size() > 0 :
    print(-1)
    exit()
for i in res:
    print(i)