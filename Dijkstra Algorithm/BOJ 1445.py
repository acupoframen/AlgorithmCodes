import heapq
n,m=map(int,input().split())
data=list(list(input()) for _ in range(n))
temp=list(list([1e10,1e10] for _ in range(m)) for _ in range(n))
q=[]
goal=[0,0]
dx=[0,0,-1,1]
dy=[1,-1,0,0]

for i in range(n):
    for j in range(m):
        if data[i][j]=='S':
            heapq.heappush(q,[0,0,i,j])
        if data[i][j]=='F':
            goal=[i,j]
            continue
        if data[i][j]=='g':
            continue
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if data[nx][ny]=='g':
                    data[i][j]='x'
                    break

while q:
    a,b,x,y=heapq.heappop(q)
    if temp[x][y][0]>a and temp[x][y][1]>b:
        pass
    else:
        continue
    temp[x][y]=[a,b]
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if data[nx][ny]=='g':
                if temp[nx][ny][0]>a+1 and temp[nx][ny][1]>b:
                    heapq.heappush(q,[a+1,b,nx,ny])
            elif data[nx][ny]=='x':
                if temp[nx][ny][0]>a and temp[nx][ny][1]>b+1:
                    heapq.heappush(q,[a,b+1,nx,ny])
            elif data[nx][ny]=='.':
                if temp[nx][ny][0]>a and temp[nx][ny][1]>b:
                    heapq.heappush(q,[a,b,nx,ny])
            else:
                heapq.heappush(q,[a,b,nx,ny])
print(*temp[goal[0]][goal[1]])