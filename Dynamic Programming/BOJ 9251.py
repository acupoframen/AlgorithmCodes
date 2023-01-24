a=input()
b=input()
lena=len(a)
lenb=len(b)
i=0
dp=[[0 for _ in range(lenb+1)] for _ in range(lena+1)]

for i in range(lena):
    for j in range(lenb):
        if a[i]==b[j]:
            dp[i+1][j+1]=dp[i][j]+1
        else: 
            dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
print(dp[lena][lenb])
