import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(curr,parent):
    global nodecount
    visited[curr]= nodecount
    currval=nodecount
    nodecount+=1
    for next in data[curr]:
        if next==parent:
            continue
        if visited[next]:
            currval=min(currval,visited[next])
        else:
            child=dfs(next,curr)
            currval=min(child,currval)
            if visited[curr]<child:
                answer.append(sorted([curr,next]))
    return currval

v,e=map(int,input().split())
data=list(list() for _ in range(v+1))
visited=list(0 for _ in range(v+1))
answer=[]
nodecount=1
for _ in range(e):
    a,b=map(int,input().split())
    data[a].append(b)
    data[b].append(a)

dfs(1,0)
answer.sort()
print(len(answer))
for i in answer:
    print(*i)