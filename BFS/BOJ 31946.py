from collections import deque
n=int(input())
m=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
color=data[0][0]
visited=list(list(0 for _ in range(m)) for _ in range(n))
visited[0][0]=1
q=deque()
q.append([0,0])
jump=int(input())
while q:
    x,y=q.popleft()
    if x==n-1 and y==m-1:
        if data[n-1][m-1]==color:
            print("ALIVE")
        else:
            print("DEAD")
        exit(0)
    for i in range(x-jump,x+jump+1):
        for j in range(y-jump,y+jump+1):
            if 0<=i<n and 0<=j<m and not visited[i][j]:
                if abs(x-i)+abs(y-j)<=jump:
                    visited[i][j]=1
                    if data[i][j]==color:
                        q.append([i,j])

print("DEAD")