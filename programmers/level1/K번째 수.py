def solution(array, commands):
    answer = []
    tmp = []
    for i in range(len(commands)):
        a = commands[i][0]-1
        b = commands[i][1]
        if(a==b):
            tmp.append(array[a])
        else:
            tmp = array[a:b]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
        tmp.clear()

    return answer
