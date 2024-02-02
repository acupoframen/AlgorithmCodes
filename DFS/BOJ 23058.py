from copy import deepcopy
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=n**2
def count(data):
    temp=0
    for i in range(n):
        temp+=data[i].count(0)
    return min(n**2-temp,temp)
def dfs(data,a,b,c):
    global answer
    answer=min(answer,c+count(data))
    if a==-1:
        if b==n:
            return
        temp=deepcopy(data)       
        dfs(data,a,b+1,c)
        for i in range(n):
            temp[i][b]^=1
        dfs(temp,a,b+1,c+1)
        return
    else:
        if a==n:
            dfs(data,-1,0,c)
            return
        temp=deepcopy(data)
        dfs(data,a+1,b,c)
        for i in range(n):
            temp[a][i]^=1
        dfs(temp,a+1,b,c+1)
        return
dfs(data,0,0,0)
print(answer)