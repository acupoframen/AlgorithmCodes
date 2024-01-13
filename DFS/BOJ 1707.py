import sys
input=sys.stdin.readline
t=int(input())
sys.setrecursionlimit(2*10**4)

def dfs(i,curr):
    global flag
    val[i]=curr
    for j in data[i]:
        if val[j]==curr:
            flag=1
            return
        if val[j]==1e10:
            dfs(j,-curr)

for i in range(t):
    v,e=map(int,input().split())
    data=[[] for _ in range(v+1)]
    val=[1e10 for _ in range(v+1)]
    flag=0
    for _ in range(e):
        a,b= map(int,input().split())
        data[a].append(b)
        data[b].append(a)
    for i in range(1,v+1):
        if flag:
            break
        if val[i]==1e10:
            dfs(i,1)
        
    if flag:
        print("NO")
    else:
        print("YES")