input_n_q = input()
n = list(map(int, input_n_q.split()))[0]
q = list(map(int, input_n_q.split()))[1]

my_input = input()
my_array = list(map(int, my_input.split()))

M = int(my_array[0])
for number in my_array:
    if M < number:
        M = number

answer_array = []
result_array = []
for _ in range(M+1):
    answer_array.append(0)
    result_array.append(0)

for i in range(n):
    answer_array[my_array[i]] +=1

for i in range(2,M+1) :
    result_array[i] = result_array[i-1] + answer_array[i-1]

print_answer = []
for i in range(q):
    key_answer = int(input())
    if key_answer > M:
        print_answer.append(n)
    elif key_answer == 0:
        print_answer.append(0)
    else:
        print_answer.append(result_array[key_answer])

for item in print_answer:
    print(item)
