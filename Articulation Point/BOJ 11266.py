import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e5))
def dfs(curr,isroot):
    global nodecount
    nodecount+=1
    visited[curr]=nodecount
    currval=visited[curr]
    child=0
    for next in data[curr]:
        if not visited[next]:
            child+=1
            minchild=dfs(next,0)
            if not isroot and minchild>=visited[curr]:
                cut[curr]=1
            currval=min(currval,minchild)
        else:
            currval=min(currval,visited[next])
    if isroot and child>1:
        cut[curr]=1
    return currval
v,e=map(int,input().split())
data=list(list() for _ in range(v+1))
visited=[0 for _ in range(v+1)]
cut=list(0 for _ in range(v+1))
nodecount=0
for _ in range(e):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(1,v+1):
    if not visited[i]:
        dfs(i,1)
print(sum(cut))
for i in range(1,v+1):
    if cut[i]:
        print(i,end=" ")