import itertools

n = int(input())
num = list(map(int,input().split()))
oper = list(map(int, input().split()))
oper_list = ['+','-','x','/']
permu_oper = []
maximum = -1e9
minimum = 1e9

for i in range(len(oper)):
    for j in range(oper[i]):
        permu_oper.append(oper_list[i])

npm = list(itertools.permutations(permu_oper, len(permu_oper))) #연산자 순열

for i in npm: 
    result = num[0]
    for j in range(1, n):
        if i[j-1] == '+':
            result += num[j]
        elif i[j-1] == '-':
            result -= num[j]
        elif i[j-1] == 'x':
            result *= num[j]
        elif i[j-1] == '/':
            result = int(result / num[j])
    maximum = max(maximum, result)
    minimum = min(minimum, result)
print(maximum)
print(minimum)
