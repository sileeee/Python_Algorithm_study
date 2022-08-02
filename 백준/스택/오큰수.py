import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
s = [] # 인덱스 임시 저장소
result = [-1] * n

s.append(0)
for i in range(1, n):
    while s and arr[s[-1]] < arr[i]:
        result[s.pop()] = arr[i] 
    s.append(i)

for i in result:
    print(i, end=' ')
