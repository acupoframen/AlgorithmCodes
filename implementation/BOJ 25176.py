n,m=map(int,input().split())
ndata=list(map(int,input().split()))
mdata=list(map(int,input().split()))

answer=0
for i in range(m):
    if i>=n:
        answer=max(answer,mdata[i])
    else:
        answer=max(answer,mdata[i]-ndata[i])
print(answer) 