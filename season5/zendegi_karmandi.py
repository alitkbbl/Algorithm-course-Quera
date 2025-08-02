n = int(input())
tasks = list(map(int, input().split()))

tasks.sort()

current_time = 0
task = 0
for i in range(n):
    if current_time + 1 <= tasks[i]:
        current_time += 1
        task += 1

print(task)

