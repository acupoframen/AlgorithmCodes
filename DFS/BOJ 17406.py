from copy import deepcopy
dx=[1,0,-1,0]
dy=[0,-1,0,1]
n,m,k=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(n))
rotation=list(list(map(int,input().split())) for _ in range(k))

answer=1e10
def findmin(arr):
    return min([sum(i) for i in arr])
def rotate(arr,qu):
    a,b,c=qu
    a-=1
    b-=1
    newarr=deepcopy(arr)
    for i in range(1,c+1):
        newa=a-i
        newb=b+i
        for w in range(4):
            for d in range(i*2):
                newnewa=newa+dx[w]
                newnewb=newb+dy[w]
                newarr[newnewa][newnewb]=arr[newa][newb]
                newa=newnewa
                newb=newnewb
    return newarr

def dfs(arr,qu):
    global answer
    if sum(qu)==k:
        answer=min(answer,findmin(arr))
        return
    for i in range(k):
        if qu[i]:
            continue
        newarr=rotate(arr,rotation[i])
        qu[i]=1
        dfs(newarr,qu)
        qu[i]=0
dfs(data,[0 for _ in range(k)])
print(answer)