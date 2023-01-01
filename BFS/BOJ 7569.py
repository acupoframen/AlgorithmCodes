from collections import deque
m,n,h=map(int,input().split())
data=[[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
dx=[[0,0,1],[0,0,-1],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0]]
q=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k]==1:
                q.append([k,j,i])
def bfs():
    while q:
        x1,y1,z1=q.popleft()
        for a,b,c in dx:
            if 0<=x1+a<m and 0<=y1+b<n and 0<=z1+c<h and not data[z1+c][y1+b][x1+a]:
                q.append([x1+a,y1+b,z1+c])
                data[z1+c][y1+b][x1+a]=data[z1][y1][x1]+1
maxNum=0
def answer():
    global maxNum
    for i in range(h):
        for j in range(n):
            maxNum=max(maxNum,max(data[i][j]))
            if 0 in data[i][j]:
                return -1
    return maxNum-1

bfs()
print(answer())
