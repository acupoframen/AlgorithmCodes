from collections import deque
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=0
dx=[[-1,0],[0,1],[1,0],[0,-1]]
for k in range(0,101):
    visited=[[0 for _ in range(n)] for _ in range(n)]
    q=deque()
    temp=0
    for i in range(n):
        for j in range(n):
            if data[i][j]>k and not visited[i][j]:
                q.append([i,j])
                temp+=1
                visited[i][j]=1
                while q:
                    a,b=q.popleft()
                    visited[a][b]=1
                    for t in range(4):
                        nx=dx[t][0]+a
                        ny=dx[t][1]+b
                        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and data[nx][ny]>k:
                            visited[nx][ny]=1
                            q.append([nx,ny])
    answer=max(answer,temp)

print(answer)