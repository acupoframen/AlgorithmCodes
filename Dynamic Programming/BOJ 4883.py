t=1
while True:
    n=int(input())
    if not n:
        break
    data=list(list(map(int,input().split())) for _ in range(n))
    dp=[[0,0,0] for _ in range(n)]
    dp[0]=[1e10,data[0][1],data[0][1]+data[0][2]]
    for i in range(1,n):
        
        for j in range(3):
            if j==0:
                dp[i][0]=min(dp[i-1][0],dp[i-1][1])+data[i][0]
            elif j==1:
                dp[i][1]=min(dp[i][0],min(dp[i-1]))+data[i][1]
            else:
                dp[i][2]=min(dp[i][1],min(dp[i-1][1:3]))+data[i][2]
    
    print(f"{t}. { dp[-1][1]}")
    t+=1