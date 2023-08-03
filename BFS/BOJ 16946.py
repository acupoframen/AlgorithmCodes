import sys
from collections import deque
input=sys.stdin.readline
def BFS(x,y):
    dxx=[[-1,0],[1,0],[0,1],[0,-1]]
    q=deque()
    q.append([x,y])
    count=1
    visited[x][y]=1
    while q:
        currx,curry=q.popleft()
        group[currx][curry]=groupnum
        for dx, dy in dxx:
            nx=currx+dx
            ny=curry+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and not data[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny]=1
                count+=1
    return count

def countzero(x,y):
    dxx=[[-1,0],[1,0],[0,1],[0,-1]]
    tempList=[]
    for dx,dy in dxx:
        nx=x+dx
        ny=y+dy
        if 0<=nx<n and 0<=ny<m and group[nx][ny]:
            if group[nx][ny] in tempList:
                continue
            else:
                tempList.append(group[nx][ny])
    count=1
    for i in tempList:
        count+=zerocount[i]
        count%=10
    return count

n,m=map(int,input().split())
data=list(list(map(int,list(input().strip()))) for _ in range(n))
visited=[[0 for _ in range(m)] for _ in range(n)]
group=[[0 for _ in range(m)] for _ in range(n)]
groupnum=1
zerocount=[0]
for i in range(n):
    for j in range(m):
        if not data[i][j] and not visited[i][j]:
            count=BFS(i,j)
            zerocount.append(count)
            groupnum+=1
answer=[[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j]:
            answer[i][j]=countzero(i,j)
for i in range(n):
    print(*answer[i],sep='')