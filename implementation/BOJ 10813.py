n,m=map(int,input().split())
data=list(i for i in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data[a],data[b]=data[b],data[a]
print(*data[1:])