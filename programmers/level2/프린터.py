def solution(priorities, location):
    answer = 0
    flag = False
    idx = location
    while priorities:
        for i in range(1, len(priorities)):
            flag = False
            if priorities[0]<priorities[i]:
                priorities.append(priorities[0])
                priorities.pop(0)
                if idx == 0:
                    idx = len(priorities)-1
                else:
                    idx -=1
                flag = True
                break
        if flag==False:
            if idx == 0:
                return answer+1
            else:
                priorities.pop(0)
                idx -=1
                answer+=1
        
    return answer
