import heapq
n,m=map(int,input().split())
data=list(list(map(int,list(input()))) for _ in range(m))
q=[]
q.append([0,0,0])
currdist=list(list(1e10 for _ in range(n)) for _ in range(m))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
while q:
    d,x,y=heapq.heappop(q)
    if currdist[x][y]<d:
        continue
    if x==m-1 and y==n-1:
        print(d)
        break
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<m and 0<=ny<n:
            if data[nx][ny]:
                if d+1<currdist[nx][ny]:
                    currdist[nx][ny]=d+1
                    heapq.heappush(q,[d+1,nx,ny])
            else:
                if d<currdist[nx][ny]:
                    currdist[x][y]=d
                    heapq.heappush(q,[d,nx,ny])