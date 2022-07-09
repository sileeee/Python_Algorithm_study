# error

n = int(input())
st = []
tmp = 0

for _ in range(n):
    a, b = map(int,input().split())
    for i in range(a):
        st.append(int(input().split()))
        if i == b:
            tmp = st[-1]
        st.sort()
    for i in range(len(st)):
        if st.pop() == tmp:
            print(i+1)
        else:
            st.pop()
