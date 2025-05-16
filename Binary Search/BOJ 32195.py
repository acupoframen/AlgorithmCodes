import sys
input = sys.stdin.readline
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
foul=0
dists=list()
for i in data:
    x,y=i
    if y>=x and y>=-x:
        dists.append(x**2+y**2)
    else:
        foul+=1
q=int(input())
poss=list(int(input()) for _ in range(q))
dists.sort()
for i in poss:
    left=0
    right=len(dists)-1
    while left<=right:
        mid=(left+right)//2
        if dists[mid]<=i**2:
            left=mid+1
        else:
            right=mid-1
    print(foul,left,len(dists)-left)