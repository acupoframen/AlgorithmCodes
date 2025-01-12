import sys
input=sys.stdin.readline
n=int(input())
data=list(list() for _ in range(n+1))
dp=list(0 for _ in range(n+1))
answer=0
for i in range(1,n+1):
    cost,ncount,*li=map(int,input().strip().split())
    dp[i]=cost
    data[i]=li

for i in range(1,n+1):
    temp=0
    for j in data[i]:
        temp=max(temp,dp[j])
    dp[i]+=temp
print(max(dp))