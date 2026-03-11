from collections import deque
a,b=map(int, input().split())

board = [list(input().strip()) for _ in range(a)]

for i in range(a):
    for j in range(b):
        if board[i][j]=='I':
            start = (i,j)
            

visited = [[False]*b for _ in range(a)]

queue = deque([start])
visited[start[0]][start[1]]=True
reward = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft()
    if board[x][y] == 'P':
        reward+=1
    for dir in range(4):
        nx=x+dx[dir]
        ny=y+dy[dir]
        if 0<=nx <a and 0<=ny<b:
            if not visited[nx][ny] and board[nx][ny] != 'X':
                visited[nx][ny]=True
                queue.append((nx,ny))

if reward !=0:
    print(reward)
else:
    print('TT')