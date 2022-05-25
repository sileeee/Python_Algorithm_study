# error(시간초과)

import sys
read = lambda: sys.stdin.readline().rstrip()

line = int(input())
arr = []
global max
max = 0
position = 0

for i in range(line):
    arr.append(list(map(int, read().split())))

def triangle(sum, position, depth):
    global max
    if depth==line:
        if max<sum:
            max = sum
        return 
    triangle(sum+arr[depth][position], position, depth+1)
    if position != depth:
        triangle(sum+arr[depth][position+1], position+1, depth+1)

triangle(0, 0, 0)
print(max)
