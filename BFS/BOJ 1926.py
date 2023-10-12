from collections import deque
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))

visited=[[0 for _ in range(m)] for _ in range(n)]
count=0
maximumarea=0
dx=[0,0,-1,1]
dy=[1,-1,0,0]
for i in range(n):
    for j in range(m):
        if data[i][j]==1 and not visited[i][j]:
            visited[i][j]=1
            q=deque()
            q.append([i,j])
            count+=1
            temp=0
            while q:
                a,b=q.popleft()
                
                temp+=1
                for k in range(4):
                    if 0<=dx[k]+a<n and 0<=dy[k]+b<m and not visited[a+dx[k]][b+dy[k]]:
                        if data[dx[k]+a][dy[k]+b]==1:
                            q.append([dx[k]+a,dy[k]+b])
                            visited[dx[k]+a][dy[k]+b]=1
            maximumarea=max(maximumarea,temp)
print(count)
print(maximumarea)