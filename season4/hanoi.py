step = 1
def hanoi(n, src, dst, help):
    global step
    if n == 1:
        print(step, src, dst)
        step += 1
    else:
        hanoi(n - 1, src, help, dst)
        print(step, src, dst)
        step += 1
        hanoi(n - 1, help, dst, src)

n = int(input())
hanoi(n, 'A', 'B', 'C')