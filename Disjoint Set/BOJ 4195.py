from collections import defaultdict
t=int(input())
def find(x):
    if x!=parents[x]:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return count[x]
    parents[max(x,y)]=min(x,y)
    count[x]=count[x]+count[y]
    count[y]=count[x]
    return count[x]

for _ in range(t):
    parents=defaultdict(str)
    count=defaultdict(int)
    n=int(input())
    for i in range(n):
        a,b=input().split()
        if len(parents[a])==0:
            count[a]=1
            parents[a]=a
        if len(parents[b])==0:
            count[b]=1
            parents[b]=b
        print(union(a,b))