import sys
sys.setrecursionlimit(10**6)

input_a_b = input()
a = list(map(int, input_a_b.split()))[0]
b = list(map(int, input_a_b.split()))[1]

def found_bmm(num1 , num2):
    if  num2 == 0:
        return num1
    else:
        return found_bmm(num2 , num1 % num2)

print(found_bmm(max(a , b) , min(a , b)))