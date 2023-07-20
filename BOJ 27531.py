n=int(input())
data=[[] for _ in range(n+1)]

for _ in range(n):
    a,b,c=map(int,input().split())
    data[a]=[b,c]
visited=[0 for _ in range(n+1)]
answer=0
dp=[[1e10,1e10] for _ in range(n+1)]
for i in range(1,n+1):
    if not visited[i]:
        if i==data[i][0]:
            answer+=data[i][1]
            visited[i]=1
            continue
        elif i==data[data[i][0]][0]:
            answer+=min(data[i][1],data[data[i][0]][1])
            visited[i]=1
            visited[data[i][0]]=1
            continue
        temp=data[i][0]
        dp[i][0]=1e10
        dp[i][1]=data[i][1]
        while i!=temp:
            if data[temp][0]==i:
                dp[i][0]=dp[temp][0]+data[temp][1]
                dp[i][1]=min(dp[temp2][0]+data[temp][1],dp[temp][1])
                break
            dp[temp][1]=min(dp[temp][0], dp[temp][1])+data[temp][1]
            dp[data[temp][0]][0]=data[temp][1]
            dp[data[temp][0]][1]=data[temp][0]
            temp2=temp
            temp=data[temp][0]
        answer+=min(dp[i])
print(answer)