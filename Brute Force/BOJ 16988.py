from itertools import combinations
from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
possiblespots=list()
for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            possiblespots.append((i,j))
possibletwospots=list(combinations(possiblespots,2))
answer=0
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for twospots in possibletwospots:
    data[twospots[0][0]][twospots[0][1]]=1
    data[twospots[1][0]][twospots[1][1]]=1
    count=0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j]==2 and not visited[i][j]:
                q = deque()
                q.append((i,j))
                temp = 1
                visited[i][j] = 1
                is_isolated = True  
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                            if data[nx][ny] == 0:
                                is_isolated = False
                            elif data[nx][ny] == 2:
                                q.append((nx, ny))
                                visited[nx][ny] = 1
                                temp += 1
                if is_isolated:
                    count += temp

    answer=max(answer,count)
    data[twospots[0][0]][twospots[0][1]]=0
    data[twospots[1][0]][twospots[1][1]]=0
print(answer)