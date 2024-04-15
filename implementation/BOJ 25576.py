import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
ak=0
for _ in range(n-1):
    temp=list(map(int,input().split()))
    tempval=0
    for i in range(m):
        tempval+=abs(temp[i]-data[i])
    if tempval>2000:
        ak+=1
if ak>=(n-1)/2:
    print("YES")
else:
    print("NO")