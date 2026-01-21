n, q = map(int, input().split())
arr = list(map(int, input().split()))

set_list = []
total = 0
for item in arr :
    total += item
    set_list.append(total)

answer = []
for step in range(q):
    s,e = map(int,input().split())
    if s==0:
        answer.append(set_list[e])
        continue
    answer.append(set_list[e] - set_list[s-1] )

for item in answer:
    print(item)