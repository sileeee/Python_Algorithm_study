# error (순서를 고려 안함)

import itertools

def calc(operan, operat):
    operan = list(operan)
    sum = 0
    for i in range(len(operan)):
        if i == 0:
            sum += int(operan[i])
        else:
            if operat[i-1] == "+":
                sum += operan[i]
            else:
                sum = operan[i] - sum
    return sum


arr = []
operan = []
operat = []
num = ""
arr = input()
for i in arr:
    if i=="-" or i =="+":
        operat.append(i)
        if num!="":
            operan.append(int(num))
            num = ""
    else:
        num += i
operan.append(int(num))
minimum = sum(operan)

npm = list(itertools.permutations(operan, len(operan)))
np = list(itertools.permutations(operat, len(operat)))
for i in npm:
    for j in np:
        minimum = min(calc(i, j),minimum)
print(minimum)
