import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(m+1))
worst=0
best=n
maxParent=[i for i in range(n+1)]
minParent=[i for i in range(n+1)]
def union(a,b,parent):
    a=find(a,parent)
    b=find(b,parent)
    if a!=b:
        if a>b:
            parent[a]=b
        else:
            parent[b]=a
def find(a,parent):
    if a!=parent[a]:
        parent[a]=find(parent[a],parent)
    return parent[a]
for a,b,v in data:
    if v==1:
        pa=find(a,minParent)
        pb=find(b,minParent)
        if pa!=pb:
            best-=1
            union(a,b,minParent)
    else:
        pa=find(a,maxParent)
        pb=find(b,maxParent)
        if pa!=pb:
            worst+=1
            union(a,b,maxParent)
print(worst**2-best**2)