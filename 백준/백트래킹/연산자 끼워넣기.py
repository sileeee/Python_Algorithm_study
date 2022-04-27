# error
import itertools

n = int(input())
num = list(map(int,input().split()))
oper = list(map(int, input().split()))
oper_arr = ['+','-','x','/']
permu_oper = []
max_result = 0
min_result = sum(num)

for i in range(len(oper)):
    for j in range(oper[i]):
        permu_oper.append(oper_arr[i])

npm = list(itertools.permutations(permu_oper, len(permu_oper))) #연산자 순열

for i in npm: 
    result = num[0]
    for j in range(1, len(num)):
        if (*i) == '+':
            result += j
        if (*i) == '-':
            result -= j
        if (*i) == 'x':
            result *= j
        if (*i) == '/':
            result /= j
    max_result = max(max_result, result)
    min_result = min(min_result, result)
print(max_result)
print(min_result)
