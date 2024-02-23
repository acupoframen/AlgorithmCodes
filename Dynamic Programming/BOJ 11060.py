from collections import deque
n=int(input())
data=list(map(int,input().split()))
dp=[1e10 for _ in range(n)]
q=deque()
q.append(0)
dp[0]=0
while q:
    a=q.popleft()
    for i in range(1,data[a]+1):
        if a+i<n and dp[a+i]>dp[a]+1:
            dp[a+i]=min(dp[a+i],dp[a]+1)
            q.append(a+i)

if dp[-1]==1e10:
    print(-1)
else:
    print(dp[-1])