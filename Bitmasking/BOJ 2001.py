import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
gem=list(0 for _ in range(n+1))
for i in range(1,k+1):
    num=int(input())
    gem[num]=1<<i
data=list(list() for _ in range(n+1))
answer=0
def dfs(state,curr,count):
    global answer
    visited[state][curr]=1
    if curr==1:
        answer=max(answer,count)
    for i in range(len(data[curr])):
        nextnode,weight=data[curr][i]
        if not visited[state][nextnode] and weight>=count:
            dfs(state,nextnode,count)
        if gem[curr]!=0:
            if state & (gem[curr]):
                continue
            nextstate=state|(gem[curr])
            nextgem=count+1
            if not visited[nextstate][nextnode] and weight>=nextgem:
                dfs(nextstate,nextnode,nextgem)
for _ in range(m):
    a,b,c=map(int,input().split())
    data[a].append([b,c])
    data[b].append([a,c])

visited=list(list(0 for _ in range(101)) for _ in range(1<<16))
data[1].append([1,100])
dfs(0,1,0)
print(answer)