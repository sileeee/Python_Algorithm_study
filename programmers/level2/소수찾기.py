#error
import itertools

def solution(numbers):
    answer = 0
    arr = []
    
    for i in range(1, len(numbers)+1):
        per = itertools.permutations(numbers, i)
        for j in per:
            perStr = ''.join(j)
            arr.append(perStr)
    arr = set(arr)
    
    for i in arr:
        if int(i) == 1:
            continue
        for j in range(2, int(i)):
            if int(i)%j == 0:
                continue
        answer +=1
               
        
    return answer
