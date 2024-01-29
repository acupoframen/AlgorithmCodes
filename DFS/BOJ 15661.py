import sys
input=sys.stdin.readline
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=1e10
visited=[0 for _ in range(n)]

def dfs(i):
    global answer
    if i==n:
        temp=0
        for i in range(n):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    temp+=data[i][j]
                    temp+=data[j][i]
                elif not visited[i] and not visited[j]:
                    temp-=data[i][j]
                    temp-=data[j][i]
        answer=min(abs(temp),answer)
        return
    visited[i]=1
    dfs(i+1)
    visited[i]=0
    dfs(i+1)

dfs(0)
print(answer)