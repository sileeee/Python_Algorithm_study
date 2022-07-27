# error
n = int(input())
arr = [x+1 for x in range(n)]
answer = []
s = []

for _ in range(n):
    answer.append(int(input()))

for i in answer:
        if len(s)!=0 and s[-1] == i:
            s.pop()
            print("-")
            continue
        for j in arr: # 멈춘 인덱스 기록해야함
            if i != j and i > j:
                s.append(j)
                print("+")
            elif i == j:
                s.append(j)
                s.pop()
                print("-")
                break
            elif i < j : 
                print("NO")
if len(s)!=0:
    print("NO")
