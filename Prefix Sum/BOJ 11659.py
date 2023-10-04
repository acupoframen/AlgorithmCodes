import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
sumdata=[0]
temp=0
for i in range(n):
    temp+=data[i]
    sumdata.append(temp)

for _ in range(m):
    a,b=map(int,input().split())
    print(sumdata[b]-sumdata[a-1])
