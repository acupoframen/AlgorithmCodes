import sys
input=sys.stdin.readline
n,p=map(int,input().split())
data=[1e10]+list(int(input()) for _ in range(n))

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b
dist=[]
for _ in range(p):
    a,b,c=map(int,input().split())
    dist.append([a,b,data[a]+data[b]+2*c])
dist.sort(key=lambda x: x[2])
parents=[i for i in range(n+1)]
answer=min(data)
count=1
for i in dist:
    a,b,c=i
    if find(a)!=find(b):
        union(a,b)
        answer+=c
        count+=1
        if count==n:
            break
print(answer)