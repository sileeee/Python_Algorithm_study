def solution(s):
    answer = ""
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    i = 0
    while(i<len(s)):
        if ord(s[i]) > 64:
            for j in range(3,6):
                a = s[i:i+j]
                if a in eng:
                    answer += str(eng.index(a))
                    i += j
                    break
                else : 
                  continue
        else:
            answer += s[i]
            i +=1
    return int(answer)
