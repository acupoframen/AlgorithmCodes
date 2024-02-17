import sys
sys.setrecursionlimit(int(1e5+1))
n,m=map(int,input().split())

data=list(i for i in range(n+1))
def find(a):
    if data[a]!=a:
        data[a]=find(data[a])
    return data[a]

def union (a,b):
    a=find(a)
    b=find(b)
    if a<b:
        data[b]=a
    else:
        data[a]=b

for _ in range(m):
    k,a,b=map(int,input().split())

    if not k:
        union(a,b)
    else:
        if find(a)==find(b):
            print("yes")
        else:
            print("no")