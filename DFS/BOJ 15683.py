import copy
n,m=map(int,input().split())
cctv=[]
data=[]
mode=[[],[[0],[1],[2],[3]], [[0,2],[1,3]], [[0,1],[1,2],[2,3],[0,3]], [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],[[0,1,2,3]]]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    da=list(map(int,input().split()))
    data.append(da)
    for j in range(m):
        if da[j] in [1,2,3,4,5]:
            cctv.append([da[j],i,j])

def fill(b,ma,x,y):
    
    for i in ma:
        nx=x
        ny=y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if b[nx][ny]==6:
                break
            elif not b[nx][ny]:
                b[nx][ny]=7
answer=1e10
def dfs(d,arr):
    global answer
    if d==len(cctv):
        count=0
        for i in range(n):
            count+=arr[i].count(0)
        answer=min(answer,count)
        return
    temp=copy.deepcopy(arr)
    cctvnum,x,y=cctv[d]
    for j in mode[cctvnum]:
        fill(temp,j,x,y)
        dfs(d+1,temp)
        temp=copy.deepcopy(arr)

dfs(0,data)
print(answer)