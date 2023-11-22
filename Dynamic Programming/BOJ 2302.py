n=int(input())
m=int(input())
vip=[]
for _ in range(m):
    vip.append(int(input()))
dp=[0] *(n+1)
dp[0]=1
dp[1]=1
if n>=2:
    dp[2]=2
for i in range(3,n+1):
    dp[i]=dp[i-1]+dp[i-2]
answer=1
if m>=1:
    temp=0
    for i in range(m):
        answer*=dp[vip[i]-1-temp]
        temp=vip[i]
    answer*=dp[n-temp]
else:
    answer=dp[n]
print(answer)