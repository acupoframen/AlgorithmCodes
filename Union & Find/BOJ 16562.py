from collections import defaultdict
n,m,k=map(int,input().split())
data=[0]+list(map(int,input().split()))
parents=[i for i in range(n+1)]
def find(x):
    if x!=parents[x]:
        parents[x]=find(parents[x])
    return parents[x]
def merge(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

for _ in range(m):
    a,b=map(int,input().split())
    merge(a,b)

for i in range(1,n+1):
    parents[i]=find(parents[i])

d=defaultdict(list)
for i in range(1,n+1):
    d[parents[i]].append(i)
answer=0
for i in d.values():
    temp=1e10
    for j in i:
        temp=min(temp,data[j])
    answer+=temp
if k<answer:
    print("Oh no")
else:
    print(answer)