import sys
read = lambda: sys.stdin.readline().rstrip()

# 첫번째 전봇대에서 1부터 차례대로 두번째 전봇대의 도착지점을 나열하면 아래와 같다.
# 8 2 9 1 4 6 7 10 
# 1 1 2 1 2 3 4 5 
# 여기서 가장 긴 증가하는 수열을 찾고 총 전깃줄 수에서 빼면 된다.
# => 8-5 = 3

n = int(input())
arr = []
line = []
increase = [1 for _ in range(n)]

for i in range(n):
    arr.append(list(map(int, read().split())))
arr.sort()

for i in range(n):
    line.append(arr[i][1])

for i in range(1, n):
    for j in range(i):
        if line[j]<line[i]:
            increase[i] = max(increase[i], increase[j]+1)
print(n-max(increase))
