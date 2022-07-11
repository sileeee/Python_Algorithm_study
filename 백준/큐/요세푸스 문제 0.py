n, k = map(int, input().split())
q = [x+1 for x in range(n)]
result = []
key = 0
while(True):
    key = (key + k - 1)%len(q)
    result.append(q.pop(key))
    if len(q) == 0:
        break

print("<%s>" %(", ".join(map(str,result))))
