n=int(input())
rank=list(map(int,input().split()))
s=input()
dp=[0 for _ in range(n)]
ranklist={'B':[0,rank[0]-1],'S':[rank[0],rank[1]-1],'G':[rank[1],rank[2]-1],'P':[rank[2],rank[3] -1],'D':[rank[3],rank[3]*2]}
if s[0]=='D':
    dp[0]=rank[3]
else:
    dp[0]=ranklist[s[0]][1]

for i,r in enumerate(s[1:]):
    i+=1
    if r=='D':
        dp[i]=rank[3]
        continue
    val=dp[i-1]+dp[i]
    if val<ranklist[r][1]:
        dp[i]=ranklist[r][1]-dp[i-1]
    elif val>ranklist[r][1]:
        dp[i]=0
        dp[i-1]=ranklist[r][1]
        for j in range(i-1,0,-1):
            if dp[j]+dp[j-1]<ranklist[s[j]][0]:
                dp[j-1]=ranklist[s[j]][0]-dp[j]
            elif dp[j]+dp[j-1]>ranklist[s[j]][1]:
                dp[j-1]=ranklist[s[j]][1]-dp[j]
            else:
                break
print(sum(dp))