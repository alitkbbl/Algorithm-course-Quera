input_n_k = input()
n = list(map(int, input_n_k.split()))[0]
k = list(map(int, input_n_k.split()))[1]

input_array = input()
my_array = list(map(int, input_array.split()))
answers_for_each_one = []

for i in range(n) :
    count = 0
    for to_change in range(n) :
        result = (to_change - i) * k + my_array[i] -   my_array[to_change]
        count += abs(result)
    answers_for_each_one.append(count)

print(min(answers_for_each_one))