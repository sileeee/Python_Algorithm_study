def solution(numbers, target):
    global answer 
    answer = 0
    sum = 0
    depth = 0

    dfs(depth, numbers, sum, target)
    return answer

def dfs(depth, numbers, sum, target):
    global answer
    if(depth == len(numbers)):
        if(sum != target):
            return
        else:
            answer += 1
            return 
    dfs(depth+1, numbers, sum+numbers[depth], target)
    dfs(depth+1, numbers, sum-numbers[depth], target)
