n=int(input())
m=int(input())
parents=[i for i in range(n+1)]

def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<=y:
        parents[x]=y
    else:
        parents[y]=x

for i in range(1,n+1):
    temp=list(map(int,input().split()))
    for j in range(n):
        if temp[j]==1:
            union(j+1,i)

city=list(map(int,input().split()))

for i in range(1,len(city)):
    if find(city[i])!=find(city[0]):
        print("NO")
        exit(0)
print("YES")