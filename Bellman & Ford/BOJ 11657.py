import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=[]
for _ in range(m):
    data.append(list(map(int,input().split())))
dist=[1e10]*(n+1)
dist[1]=0
for i in range(n):
    for a,b,c in data:
        if dist[a]!=1e10 and dist[b]>dist[a]+c:
            if i==n-1:
                print(-1)
                exit(0)
            dist[b]=dist[a]+c
for i in dist[2:]:
    if i==1e10:
        print(-1)
    else:
        print(i)            