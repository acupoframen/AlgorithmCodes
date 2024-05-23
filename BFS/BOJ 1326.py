from collections import deque
n=int(input())
data=[0]+list(map(int,input().split()))
a,b=map(int,input().split())
dp=[1e10 for _ in range(n+1)]

q=deque()
q.append(a)
dp[a]=0
while q:
    temp=q.popleft()
    k=data[temp]
    if temp==b:
        print(dp[b])
        exit(0)
    for i in range(temp,0,-k):
        if dp[i]==1e10:
            q.append(i)
            dp[i]=dp[temp]+1
    for i in range(temp,n+1,k):
        if dp[i]==1e10:
            q.append(i)
            dp[i]=dp[temp]+1

print(-1)