import sys
input=sys.stdin.readline
n,q=map(int,input().split())
limit=[1e10]+list(int(input()) for _ in range(n))
drank=[0 for _ in range(n+2)]
parent=[i for i in range(n+2)]
def find(n):
    if parent[n]!=n:
        parent[n]=find(parent[n])
    return parent[n]
def union(a,b):
    a=find(parent[a])
    b=find(parent[b])
    if a>b:
        parent[b]=a
    else:
        parent[a]=b
    
for _ in range(q):
    op,*num=map(int,input().split())
    if op==1:
        player=find(num[0])
        liter=num[1]
        while player<=n:
            if drank[player]+liter<limit[player]:
                drank[player]+=liter
                break
            elif drank[player]+liter==limit[player]:
                drank[player]+=liter
                union(player,player+1)
                break
            else:
                liter-=(limit[player]-drank[player])
                drank[player]=limit[player]
                union(player,player+1)
                player+=1
    else:
        print(drank[num[0]])