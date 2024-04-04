import sys
input=sys.stdin.readline
n=int(input())
parents=[i for i in range(n+1)]
def find(n):
    if parents[n]!=n:
        parents[n]=find(parents[n])
    return parents[n]

def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        parents[b]=a
    else:
        parents[a]=b
data=[[0,0,0,0]]
for i in range(n):
    x1,y1,x2,y2=map(int,input().split())
    x1,x2=min(x1,x2),max(x1,x2)
    y1,y2=min(y1,y2),max(y1,y2)
    data.append([x1,y1,x2,y2])

for i in range(n):
    x1,y1,x2,y2=data[i]
    for j in range(i+1,n+1):
        x3, y3, x4, y4 = data[j]
        if x3>x1 and x2>x4 and y3>y1 and y2>y4:
            continue
        if x1>x3 and x4>x2 and y1>y3 and y4>y2:
            continue
        if x3>x2 or x1>x4 or y3>y2 or y1>y4:
            continue
        union(i,j)
for i in range(n+1):
    find(i)
print(len(set(parents))-1)
