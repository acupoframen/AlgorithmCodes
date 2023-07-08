n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
parents=[x for x in range(n)]

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)

def check(x1,y1,x2,y2,x3,y3,x4,y4):
    ccw1=ccw(x1,y1,x2,y2,x3,y3)
    ccw2=ccw(x1,y1,x2,y2,x4,y4)
    ccw3=ccw(x3,y3,x4,y4,x1,y1)
    ccw4=ccw(x3,y3,x4,y4,x2,y2)
    if ccw1*ccw2==0 and ccw3*ccw4==0:
        if ccw1*ccw2==0 and ccw3*ccw4==0:
            minx1=min(x1,x2)
            minx2=min(x3,x4)
            maxx1=max(x1,x2)
            maxx2=max(x3,x4)
            miny1=min(y1,y2)
            miny2=min(y3,y4)
            maxy1=max(y1,y2)
            maxy2=max(y3,y4)
            if minx1 <= maxx2 and maxx1>=minx2 and miny1<=maxy2 and maxy1>=miny2:
                return True
    elif ccw1*ccw2 <=0 and ccw3*ccw4 <=0:
        return True
    return False

def findParents(a):
    if parents[a]!=a:
        parents[a]=findParents(parents[a])
    return parents[a]

def union(a,b):
    a=findParents(a)
    b=findParents(b)
    if a>b:
        parents[a]=b
    else:
        parents[b]=a

for i in range(n):
    for j in range(i,n):
        val=check(*data[i], *data[j])
        if val:
            union(i,j)

for i in range(n):
    parents[i]=findParents(i)
answer=[0 for _ in range(n)]
count=0
for i in range(n):
    if i==parents[i]:
        count+=1
    answer[findParents(i)]+=1
print(count)
print(max(answer))