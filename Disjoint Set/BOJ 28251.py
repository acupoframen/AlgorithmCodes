import sys
input=sys.stdin.readline
n,q=map(int,input().split())
data=[0]+list(map(int,input().split()))
parents=[i for i in range(n+1)]
answer=[0 for _ in range(n+1)]
def find(a):
    if a!=parents[a]:
        parents[a]=find(parents[a])
    return parents[a]

def union(a,b):
    a=find(a)
    b=find(b)
    a,b=min(a,b),max(a,b)
    if a!=b:
        parents[b]=a
        answer[a]+= data[a]*data[b]+answer[b]
        data[a]+=data[b]
    print(answer[a])

for _ in range(q):
    a,b=map(int,input().split())
    union(a,b)