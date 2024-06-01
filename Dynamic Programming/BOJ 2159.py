n=int(input())
x,y=map(int,input().split())
data=[[x,y]]+list(list(map(int,input().split())) for _ in range(n))
dp=[[1e10 for _ in range(5)] for _ in range(n+1)]
for k in range(4):
    dp[0][k]=1
dp[0][4]=0
dx=[0,0,-1,1,0]
dy=[1,-1,0,0,0]
for i in range(1,n+1):
    for k in range(5):
        nx,ny=data[i][0]+dx[k],data[i][1]+dy[k]
        temp=1e10
        for j in range(5):
            x,y=data[i-1][0]+dx[j],data[i-1][1]+dy[j]
            temp=min(temp,abs(x-nx)+abs(y-ny)+dp[i-1][j])
        dp[i][k]=temp

print(min(dp[-1]))