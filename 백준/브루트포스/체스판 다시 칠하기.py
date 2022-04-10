m, n = map(int, input().split())
board = []
w_sum = 0
b_sum = 0
total = []

for i in range(m):
  x = input()
  board.append(list(x)) # 문자열을 한 문자씩 리스트로 넣음
for a in range(m-7):
  for b in range(n-7):
    b_sum = 0
    w_sum = 0
    for i in range(a, a+8):
      for j in range(b, b+8):
        if((i+j)%2==0):
          if(board[i][j]!='W'): 
            w_sum +=1 # W부터 시작할 때
          if(board[i][j]!='B'): 
            b_sum +=1 # B부터 시작할 때
        else:
          if(board[i][j]!='W'):
            b_sum +=1
          if(board[i][j]!='B'):
            w_sum +=1
    total.append(w_sum)
    total.append(b_sum)
print(min(total))
