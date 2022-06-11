# error (다른 테스트케이스에서 indexerror 발생 ㅠ)

arr = []
for _ in range(2):
    arr.append(list(str(input())))

lcs = [[0]*(len(arr[0])+1) for _ in range(len(arr[1])+1)]
# arr[0] : ACAYKP
# arr[1] : CAPCAK

for i in range(1, len(arr[0])+1):
    for j in range(1, len(arr[1])+1):
        if arr[0][i-1]==arr[1][j-1]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])
