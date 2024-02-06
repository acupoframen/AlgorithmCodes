import sys
input=sys.stdin.readline

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,q=map(int,input().split())
parent=[i for i in range(n+1)]
data=[[0]]
for i in range(1,n+1):
    a,b,c=map(int,input().split())
    data.append([a,b,c,i])

data.sort()

a,b,c,i=data[1]
for j in range(2,n+1):
    nexta,nextb,nextc,nexti=data[j]
    if nexta<=b:
        union(i,nexti)
        if nextb>=b:
            a,b,c,i=nexta,nextb,nextc,nexti
    else:
        a,b,c,i=nexta,nextb,nextc,nexti

for _ in range(q):
    a,b=map(int,input().split())
    if find(a)==find(b):
        print(1)
    else:
        print(0)