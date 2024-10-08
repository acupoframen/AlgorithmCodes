import sys
sys.setrecursionlimit(int(2e5))
input=sys.stdin.readline
n=int(input())
data=list([0,0] for _ in range(n+1))
roads=list(list() for _ in range(n+1))
for i in range(2,n+1):
    a,b,c=input().split()
    b=int(b)
    c=int(c)
    if a=='S':
        data[i][0]=b
    else:
        data[i][1]=b
    roads[c].append(i)
def dfs(node):
    sheeps=data[node][0]
    for i in roads[node]:
        sheeps+=dfs(i)
    if data[node][1]:
        if sheeps<data[node][1]:
            data[node][1]-=sheeps
            sheeps=0
        else:
            sheeps-=data[node][1]
            data[node][1]=0
    return sheeps
print(dfs(1))