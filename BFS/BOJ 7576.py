from collections import deque
m,n=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
q=deque()
for i in range(n):
    for j in range(m):
        if data[i][j]==1:
            q.append([i,j])
dx=[[-1,0],[1,0],[0,1],[0,-1]]
day=0
def bfs():
    global day
    while q:
        coord=q.popleft()
        for x1,y1 in dx:
            if 0<=coord[0]+x1<n and 0<=coord[1]+y1<m and not data[coord[0]+x1][coord[1]+y1]:
                data[coord[0]+x1][coord[1]+y1]+=(data[coord[0]][coord[1]]+1)
                q.append([coord[0]+x1,coord[1]+y1])
            
bfs()
for i in range(n):
    day=max(day,max(data[i]))
    if 0 in data[i]:
        day=0
        break
print(day-1)
            
