st='-'+input()
length=len(st)
dp=[0 for _ in range(1001)]
for i in range(1,length):
    for j in range(i,length):
        if st[i]==st[j]:
            dp[j]+=1
            for k in range(j,length-1):
                dp[j]+=dp[k+1]
            dp[j]%=10007

answer=0
for i in range(1,length):
    answer+=dp[i]

print(answer%10007)