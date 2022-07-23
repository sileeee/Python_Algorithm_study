import sys
n = int(input())
read = []
st = []

for _ in range(n):
    read = sys.stdin.readline().rstrip()
    if len(read)>5:
        st.append(read.split()[1])
    elif read == 'pop':
        if len(st)==0:
            print(-1)
        else:
            print(st.pop())
    elif read == 'size':
        print(len(st))
    elif read == 'empty':
        if len(st) == 0:
            print(1)
        else : 
            print(0)
    else : 
        if len(st) == 0:
            print(-1)
        else:
            top = st.pop()
            print(top)
            st.append(top)
