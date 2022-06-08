# error

arr = []
for _ in range(2):
    arr.append(list(str(input())))  
lcs = [0,0]
pos = 0
pos_tmp = 0
for j in range(2):
    pos_tmp = 0
    pos = 0
    for i in arr[0+j]:
        #print(arr[1][pos])
        while(pos_tmp != len(arr[1-j])):
            if pos == len(arr[1]):
                pos = pos_tmp
                break
            if i == arr[1-j][pos]:
                pos+=1
                pos_tmp = pos
                lcs[j] +=1
                break
            pos+=1
print(max(lcs))
