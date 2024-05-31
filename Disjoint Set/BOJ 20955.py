import sys
input=sys.stdin.readline
n,m=map(int,input().split())
parents=[i for i in range(n+1)]
def find(x):
    if parents[x]!=x:
        parents[x]=find(parents[x])
    return parents[x]

answer=0
def merge(x,y):
    global answer
    x=find(x)
    y=find(y)
    if x==y:
        answer+=1
    elif x<=y:
        parents[y]=x
    else:
        parents[x]=y

for _ in range(m):
    u,v=map(int,input().split())
    merge(u,v)
for i in range(1,n+1):
    parents[i]=find(parents[i])
print(answer+len(set(parents[1:]))-1)