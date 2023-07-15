from collections import deque
t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    data=[[0 for _ in range(n)] for _ in range(m) ]
    for _ in range(k):
        a,b=map(int,input().split())
        data[a][b]=1
    q=deque()
    answer=0
    dx=[[0,1],[0,-1],[1,0],[-1,0]]
    for i in range(m):
        for j in range(n):
            if data[i][j]==1:
                answer+=1
                q.append([i,j])
                data[i][j]=0
                while q:
                    i2,j2=q.popleft()
                    for k in range(4):
                        nx=dx[k][0]+i2
                        ny=dx[k][1]+j2
                        if 0<=nx<m and 0<=ny<n and data[nx][ny]==1:
                            data[nx][ny]=0
                            q.append([nx,ny])
    print(answer)