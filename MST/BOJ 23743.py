n,m=map(int,input().split())
data=list()
for _ in range(m):
    a,b,c=map(int,input().split())
    data.append([c,a,b])

parents=[i for i in range(n+1)]
def find(a):
    if a!=parents[a]:
        parents[a]=find(parents[a])
    return parents[a]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[b]=a
    else:
        parents[a]=b

val=list(map(int,input().split()))
for i in range(1,n+1):
    data.append([val[i-1],i,0])

data.sort()
answer=0

for i in range(len(data)):
    c,a,b=data[i]
    if find(a)!=find(b):
        union(a,b)
        answer+=c

print(answer)