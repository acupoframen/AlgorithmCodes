def check():
    for i in range(n):
        curr=i
        for j in range(h):
            if data[j][curr]:
                curr+=1
            elif curr>0 and data[j][curr-1]:
                curr-=1
        if curr!= i:
            return False
    return True
def dfs(count,x,y):
    global answer
    if check():
        answer=min(answer,count)
        return 
    elif count==3 or answer<=count:
        return
    for i in range(x,h):
        if i==x:
            curr=y
        else:
            curr=0
        for j in range(curr,n-1):
            if not data[i][j] and not data[i][j+1]:
                if j>0 and data[i][j-1]:
                    continue
                data[i][j]=1
                dfs(count+1,i,j+1)
                data[i][j]=0

n,m,h=map(int,input().split())
data=[[0 for _ in range(n)] for _ in range(h)]
answer=1e10
for _ in range(m):
    a,b=map(int,input().split())
    data[a-1][b-1]=1
dfs(0,0,0)
if answer==1e10:
    print (-1)
else:
    print(answer)