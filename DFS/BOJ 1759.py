from collections import deque
l,c=map(int,input().split())
data=list(input().split())
data.sort()
comb=[]
visited=[0 for _ in range(c)]
def dfs(num,d):
    if d==l:
        vcount=0
        for i in q:
            if i in ['a','e','i','o','u']:
                vcount+=1
                
        if 1<=vcount<=l-2:
            comb.append(list(q))
    
    for i in range(c):
        if i<num:
            continue
        if not visited[i]:
            visited[i]=1
            q.append(data[i])
            dfs(i,d+1)
            visited[i]=0
            q.pop()
q=deque([])
dfs(0,0)
for i in comb:
    print("".join(i))