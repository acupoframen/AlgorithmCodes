n,m=map(int,input().split())
parents=[i for i in range(n)]
data=[list(map(int,input().split())) for _ in range(m)]

def find(a):
    if parents[a]!=a:
        parents[a]=find(parents[a])
    return parents[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

for i in range(m):
    a,b=data[i]
    if find(a)==find(b):
        print(i+1)
        exit(0)
    union(a,b)
print(0)