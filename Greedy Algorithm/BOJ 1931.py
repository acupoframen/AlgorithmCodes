import sys
input=sys.stdin.readline
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
data.sort(key=lambda x:[x[1],x[0]])
start,end=data[0]
cnt=1
for i in range(1,n):
    start1,end1=data[i]
    if end<=start1:
        start,end=start1,end1
        cnt+=1
print(cnt)