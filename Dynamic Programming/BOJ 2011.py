data='0'+input()
dp=list(0 for _ in range(len(data)+1))
dp[0]=1
dp[1]=1
if data[1]=='0':
    print(0)
    exit(0)
for i in range(1,len(data)):
    if 10<=int(data[i-1:i+1])<=26:
        dp[i+1]+=dp[i-1]
    if int(data[i])>0:
        dp[i+1]+=dp[i]
    dp[i+1]%=1000000
print(dp[len(data)])