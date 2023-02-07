import sys
input=sys.stdin.readline
n=int(input())
ndata=list(map(int,input().split()))
m=int(input())
mdata=list(list(map(int,input().split())) for _ in range(m))
dp=[[0 for _ in range(n)] for _ in range(n)]
for index in range(n):
    for start in range(n):
        end=start+index
        if end>=n:
            break
        if start==end:
            dp[start][end]=1
            continue
        if end==start+1 and ndata[start]==ndata[end]:
            dp[start][end]=1
            continue
        if ndata[start]==ndata[end] and dp[start+1][end-1]:
            dp[start][end]=1
for i in range(m):
    a,b=mdata[i]
    print(dp[a-1][b-1])