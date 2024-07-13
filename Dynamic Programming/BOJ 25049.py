n=int(input())
data=list(map(int,input().split()))
dp1=list(0 for _ in range(n))
maxdp1=list(0 for _ in range(n))
dp2=list(0 for _ in range(n))
dp1[0]=data[0]
maxdp1[0]=data[0]
for i in range(1,n):
    dp1[i]=max(dp1[i-1]+data[i],data[i])
    maxdp1[i]=max(maxdp1[i-1],dp1[i])
maxdp2=list(0 for _ in range(n))
maxdp2[n-1]=data[n-1]
dp2[n-1]=data[n-1]
for i in range(n-2,-1,-1):
    dp2[i]=max(dp2[i+1]+data[i],data[i])
    maxdp2[i]=max(maxdp2[i+1],dp2[i])

answer=max(0,maxdp1[n-1])
for i in range(n-2):
    answer=max(answer,maxdp1[i]+maxdp2[i+1])

print(sum(data)+answer)