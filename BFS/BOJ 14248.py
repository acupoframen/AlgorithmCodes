from collections import deque
n=int(input())
q=deque()
data=list(map(int,input().split()))
s=int(input())
dp=[0 for _ in range(n+1)]
q.append(s-1)
dp[s-1]=1
while q:
    i=q.popleft()
    if i-data[i]>=0 and dp[i-data[i]]==0:
        dp[i-data[i]]=1
        if i<n:
            q.append(i-data[i])
    if i+data[i]<n and dp[i+data[i]]==0:
        dp[i+data[i]]=1
        if i<n:
            q.append(i+data[i])
print(dp.count(1))