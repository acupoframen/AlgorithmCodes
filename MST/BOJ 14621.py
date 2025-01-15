import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e4))
import heapq 
n,m=map(int,input().split())
gender=[0]+list(input().split())
parents=list(i for i in range(n+1))
q=[]
for _ in range(m):
    x,y,w=map(int,input().split())
    heapq.heappush(q,[w,x,y])
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]
def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y
answer=0
while q:
    w,x,y=heapq.heappop(q)
    if find(x) != find(y) and gender[x] != gender[y]:
        union(x,y)
        answer+=w

for i in range(1,n+1):
    if find(1)!=find(i):
        print(-1)
        exit(0)
print(answer)