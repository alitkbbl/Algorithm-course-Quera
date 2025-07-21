import sys
sys.setrecursionlimit(10**6)

def gray_code(length):
    if length == 0:
        return ['']
    g1 = gray_code(length - 1)
    g2 = g1[::-1]
    for i in range(len(g1)):
        g1[i] = '0' + g1[i]
        g2[i] = '1' + g2[i]
    return g1 + g2

n = int(input())
result = gray_code(n)
for code in result:
    print(code)
