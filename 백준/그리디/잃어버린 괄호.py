arr = []
operan = []
operat = []
num = ""
result = 0

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

i = 0
while(operat and i<len(operat)) :
    if operat[i] == "+":
        tmp = operan[i] + operan[i+1]
        del operan[i+1]
        operan[i] = tmp
        tmp = 0
        del operat[i]
    else : 
        i += 1

result = operan[0]
for i in range(len(operat)):
    result -= operan[i+1]

print(result)
