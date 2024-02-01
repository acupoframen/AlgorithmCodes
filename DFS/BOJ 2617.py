n,m=map(int,input().split())
heavier=[[] for _ in range(n+1)]
lighter=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    heavier[a].append(b)
    lighter[b].append(a)

answer=0
mid=(n+1)//2
def dfs(i,new):
    global visited
    global temp
    visited[i]=1
    for j in new[i]:
        if not visited[j]:
            temp+=1
            dfs(j,new)

for i in range(1,n+1):
    visited=[0 for _ in range(n+1)]
    temp=0
    dfs(i,heavier)
    if temp>=mid:
        answer+=1
        continue
    temp=0
    dfs(i,lighter)
    if temp>=mid:
        answer+=1
        continue

print(answer)