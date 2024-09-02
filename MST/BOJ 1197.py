import sys
sys.setrecursionlimit(int(1e4))
input=sys.stdin.readline
v,e=map(int,input().split())
parent=[i for i in range(v+1)]
edges=[]

for i in range(e):
    a,b,v=map(int,input().split())
    edges.append([v,a,b])

def find(n):
    if n!=parent[n]:
        parent[n]=find(parent[n])
    return parent[n]

edges.sort()
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a>b:
            parent[a]=b
        else:
            parent[b]=a
answer=0
while edges:
    v,a,b=edges[0]
    pa=find(a)
    pb=find(b)
    if pa!=pb:
        answer+=v
        union(a,b)
    del edges[0]

print(answer)