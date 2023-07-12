import sys
input=sys.stdin.readline
def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return x
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
n,m,k=map(int,input().split())
gen=list(map(int,input().split()))
lines=[list(map(int,input().split())) for _ in range(m)]
parent=[0]*(n+1)
for i in range(1,n+1):
    if i in gen:
        continue
    parent[i]=i
result=0
lines.sort(key=lambda x: x[2])
for i in lines:
    a,b,val=i
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=val
print(result)