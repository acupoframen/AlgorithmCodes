n,k=map(int,input().split())
data=list(map(int,input().split()))
dp=list(0 for _ in range(n+1))
for i in data:
    dp[i]=1e10
maxNum=n
for i in range(1,n+1):
    if i+k>n:
        break
    if all(x==1e10 for x in dp[i:i+k]):
        maxNum=i-1
        break

for i in range(maxNum,0,-1):
    if dp[i]==1e10:
        continue
    allzero=1
    for j in range(i+1,i+k+1):
        if j>n:
            break
        if dp[j]==1e10:
            continue
        elif dp[j]==1:
            allzero=0
            break
    dp[i]=allzero
for i in range(1,min(n,k)+1):
    if dp[i]==1:
        print(1)
        exit(0)
print(0)