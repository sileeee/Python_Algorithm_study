zero = [1, 0, 1] #f(0) f(1) f(2)
one = [0, 1, 1] #f(0) f(1) f(2)

def fibo(num):
    if len(zero) <= num:
        for i in range(len(zero), num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[num], one[num]))

n = int(input())
for _ in range(n):
    fibo(int(input()))
