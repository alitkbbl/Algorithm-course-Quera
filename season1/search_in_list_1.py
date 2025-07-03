input_n_q = input()
n = list(map(int, input_n_q.split()))[0]
q = list(map(int, input_n_q.split()))[1]

input_array = input()
my_array = list(map(int, input_array.split()))
answer_array = []
for i in range(q):
    key_answer = int(input())
    result = 0
    for element in my_array:
        if key_answer > element:
            result = result+1
    answer_array.append(result)

for item in answer_array:
    print(item)
