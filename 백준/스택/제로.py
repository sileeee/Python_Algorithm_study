n = int(input())
st = []

for i in range(n): 
  num = int(input())
  if(num == 0): 
    st.pop()
  else:
    st.append(num) 
print(sum(st))
