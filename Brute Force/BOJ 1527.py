from collections import deque
a,b=map(int,input().split())
temp=0
dp=['4','7']
q=deque(['4','7'])
while q:
    num=q.popleft()
    if int(num+'4')<1000000000:
        dp.append(num+'4')
        q.append(num+'4')
    if int(num+'7')<1000000000:
        dp.append(num+'7')
        q.append(num+'7')
dp=list(map(int,dp))
dp.append(1000000000)
atemp=0
btemp=len(dp)-1
for i in range(len(dp)):
    atemp=i
    if dp[i]>=a:
        atemp=i
        break
for i in range(len(dp)):
    btemp=i
    if dp[i]>b:
        btemp=i
        break

print(btemp-atemp)