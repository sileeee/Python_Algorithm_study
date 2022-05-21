# error

arr = []

def find(a, b, c):
    if((a, b, c)in arr):
        idx = arr.index(a, b, c)
        return arr[idx]
    else:
        arr.append((a, b, c))
        return 0

def w(a, b, c):
    answer = 0
    value = find(a, b, c)
    if (a <= 0 or b <= 0 or c <= 0):
        return 1
    elif (a > 20 or b > 20 or c > 20):
        return w(20, 20, 20)
    elif (a < b and b < c):
        if (value):
            return value
        else:
            w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        if (value):
            return value
        else:
            w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

while(1):
    a, b, c = map(int, input().split())
    if(a == -1 and b == -1 and c == -1):
        break
    else:
        answer = w(a, b, c)
print("w({}, {}, {}) = {}".format(a, b, c, answer))
