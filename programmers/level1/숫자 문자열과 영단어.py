def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if s.isdigit(): 
        return int(s) 
    answer = ''
    temp = ''
    for i in s:
        if i.isdigit():
            answer+=i
        else:
            temp += i
            if temp in eng:
                answer += str(eng.index(temp))
                temp = ''
 
    return int(answer)
