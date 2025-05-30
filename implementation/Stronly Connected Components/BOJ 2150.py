import sys
sys.setrecursionlimit(int(1e5)+1)

v,e=map(int,input().split())
data=list([] for _ in range(v+1))
reverseddata=list([] for _ in range(v+1))
for _ in range(e):
    a,b=map(int,input().split())
    data[a].append(b)
    reverseddata[b].append(a)

visited=list(0 for _ in range(v+1))
stack=[]
def dfs(i):
    visited[i]=1
    for j in data[i]:
        if not visited[j]:
            dfs(j)
    stack.append(i)

def reversedfs(i,scc):
    visited[i]=1
    scc.append(i)
    for j in reverseddata[i]:
        if not visited[j]:
            reversedfs(j,scc)

for i in range(1,v+1):
    if not visited[i]:
        dfs(i)

visited=[0 for _ in range(v+1)]
answer=[]
while stack:
    scc=[]
    i=stack.pop()
    if not visited[i]:
        reversedfs(i,scc)
        answer.append(sorted(scc))

print(len(answer))
answer.sort()
for i in answer:
    print(*i,-1)