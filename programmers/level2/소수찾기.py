import itertools

def solution(numbers):
    answer = 0
    arr = set()
    flag = True

    for i in range(1, len(numbers)+1):
        per = set(map(int, map(''.join, itertools.permutations(list(numbers), i))))
        arr |= per # 합집합
    arr -= set(range(0, 2))

    for i in arr:
        flag = True
        for j in range(2, i):
            if i%j == 0:
                flag = False
                break
        if(flag == True):
            answer +=1

    return answer
