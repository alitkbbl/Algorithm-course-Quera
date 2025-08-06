n = int(input())
org = ['' for x in range(n)]
seen = [False for x in range(n)]
for i in range(n):
    org[i] = input()

answer = 0
q = int(input())
for x in range(q):
    cur = input()
    # Find 'cur' in 'org'
    for i in range(n):
        if cur == org[i]:
            seen[i] = True

    # If we saw all organization 'All' will be 'True' otherwise 'False'
    All = True
    for x in seen:
        if not x:
            All = False

    # If we saw all organization
    if All:
        # suppose that we didn't see any organization
        for i in range(n):
            seen[i] = False
        # We sold information to 'cur', so we should sell remain info to another co.
        answer += 1
        # 'cur' is as cuurent input, we should do something
        for i in range(n):
            if cur == org[i]:
                seen[i] = True
print(answer)