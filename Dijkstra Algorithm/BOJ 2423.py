import heapq
dx1=[[1,1],[-1,-1],[1,-1],[-1,1]]
n,m=map(int,input().split())
data=[list(input()) for _ in range(n)]
dists=[[1e10 for _ in range(m+1)] for _ in range(n+1)]
answer=1e10
def dijkstra():
    global answer
    q=[]
    heapq.heappush(q,[0,0,0]) #turnaround,x,y
    dists[0][0]=0
    while q:
        dist,x,y=heapq.heappop(q)
        if x==n and y==m:
            break
        for a,b in dx1:
            if 0<=a+x<n+1 and 0<=b+y<m+1:
                if a==1 and b==1:
                    if dists[a+x][b+y]>dist:
                        if data[x][y]=='\\':
                            heapq.heappush(q,[dist,a+x,b+y])
                            dists[a+x][b+y]=dist
                        else:
                            data[x][y]=[1e10,1e10]
                            heapq.heappush(q,[dist+1,a+x,b+y])
                            dists[a+x][b+y]=dist+1
                elif a==1 and b==-1:
                    if dists[a+x][b+y]>dist:
                        if data[x][y-1]=='/':
                            data[x][y-1]=[1e10,1e10]
                            heapq.heappush(q,[dist,a+x,b+y])
                            dists[a+x][b+y]=dist
                        else:
                            data[x][y-1]=[1e10,1e10]
                            heapq.heappush(q,[dist+1,a+x,b+y])
                            dists[a+x][b+y]=dist+1
                elif a==-1 and b==-1:
                    if dists[a+x][b+y]>dist:
                        if data[x-1][y-1]=='\\':
                            data[x-1][y-1]=[1e10,1e10]
                            heapq.heappush(q,[dist,a+x,b+y])
                            dists[a+x][b+y]=dist
                        else:
                            data[x-1][y-1]=[1e10,1e10]
                            heapq.heappush(q,[dist+1,a+x,b+y])
                            dists[a+x][b+y]=dist+1
                else:
                    if dists[a+x][b+y]>dist:
                        if data[x-1][y]=='/':
                            data[x-1][y]=[1e10,1e10]
                            heapq.heappush(q,[dist,a+x,b+y])
                            dists[a+x][b+y]=dist
                        else:
                            data[x-1][y]=[1e10,1e10]
                            heapq.heappush(q,[dist+1,a+x,b+y])
                            dists[a+x][b+y]=dist+1
    answer=min(answer,dists[n][m])
dijkstra()
if answer==1e10:
    print("NO SOLUTION")
else:
    print(answer)

