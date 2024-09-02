n=int(input())
m=int(input())
parents=[i for i in range(n+1)]
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parents[a]=b
    else:
        parents[b]=a

data=[]
for _ in range(m):
    a,b,c=map(int,input().split())
    data.append([c,a,b])
data.sort()
answer=0
for i in range(m):
    c,a,b=data[i]
    if parents[a]!=parents[b]:
        union(a,b)
        answer+=c
        for j in range(1,n+1):
            parents[j]=find(parents[j])
print(answer)