
n = int(input())
input_array = input()
my_array = list(map(int, input_array.split()))
my_array = sorted(my_array)
if len(my_array) % 2 ==0 :
    m = my_array[int(len(my_array)/2) - 1]
else:
    m = my_array[int((len(my_array)-1)/2)]

count = 0
for to_change in range(n) :
    result = my_array[to_change] - m
    count += abs(result)



print(m , count)
