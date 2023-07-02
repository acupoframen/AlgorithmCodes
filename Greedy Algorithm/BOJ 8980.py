import sys
input=sys.stdin.readline
n,c=map(int,input().split())
m=int(input())
villages=[0 for _ in range(n+1)]
data=[]
answer=0
for _ in range(m):
    data.append(list(map(int,input().split())))
data.sort(key=lambda x: (x[1],x[0]))
for start, end, count in data:
    maxCount=count
    for i in range(start, end):
        maxCount=min(maxCount,c-villages[i])
    for j in range(start,end):
        villages[j]+=maxCount
    answer+=maxCount
print(answer)