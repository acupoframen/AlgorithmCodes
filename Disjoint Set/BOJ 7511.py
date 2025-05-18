import sys
input = sys.stdin.readline

t=int(input())
scenarionum=1
def find(parents,x):
    if parents[x]!=x:
        parents[x]=find(parents,parents[x])
    return parents[x]

def union(parents,x,y):
    x=find(parents,x)
    y=find(parents,y)
    if x<y:
        parents[y]=x
    else:
        parents[x]=y

for _ in range(t):
    n=int(input())
    k=int(input())
    parents=[i for i in range(n+1)]
    data=list(list(map(int, input().split())) for _ in range(k))
    for i in data:
        union(parents,i[0],i[1])
    m=int(input())
    print(f"Scenario {scenarionum}:")
    scenarionum+=1
    for i in range(m):
        a,b=map(int,input().split())
        if find(parents,a)==find(parents,b):
            print(1)
        else:
            print(0)
    print()