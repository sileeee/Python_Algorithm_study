def fib(n) :
    global result
    if n == 1 or n == 2:
        result[0] +=1
        return 1  # 코드1
    else :
        return (fib(n - 1) + fib(n - 2))


n = int(input())
global result
result = [0, 0]
if n>2:
    result[1] = n-2
else:
    result[1] = 0
fib(n)
print('{} {}'.format(result[0], result[1]))
