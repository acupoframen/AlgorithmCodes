t=int(input())
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

def merge(x,y):
    x=find(x)
    y=find(y)
    if x>=y:
        parents[x]=y
    else:
        parents[y]=x

for _ in range(t):
    n=int(input())
    data=list(list(map(int,input().split())) for _ in range(n))
    parents=[i for i in range(n)] 
    for i in range(n-1):
        x1,y1,r1=data[i]
        for j in range(i+1,n):
            x2,y2,r2=data[j]
            if (r1+r2)**2>=(x1-x2)**2+(y1-y2)**2:
                merge(i,j)
    for i in range(n):
        parents[i]=find(parents[i])
    print(len(set(parents)))