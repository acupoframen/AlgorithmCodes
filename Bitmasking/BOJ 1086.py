import sys
import math
input=sys.stdin.readline
n=int(input())
s=list(int(input()) for _ in range(n))
k=int(input())

data=[]
dp=[[0]*k for _ in range(1<<n)]
dp[0][0]=1
for l in range(n):
    temp=[]
    for i in range(k):
        temp.append((i*(10**(len(str(s[l])))%k)+(s[l]%k))%k)
    data.append(temp)
for i in range(1<<n):
    for l in range(n):
        if i&(1<<l):
            continue
        for j in range(k):
            nextval=data[l][j]
            dp[i|(1<<l)][nextval]+=dp[i][j]
p=dp[(1<<n)-1][0]
q=sum(dp[(1<<n)-1])
g=math.gcd(p,q)
print(p//g, "/", q//g, sep="")