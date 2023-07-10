import sys
input=sys.stdin.readline
n=int(input())
data=list(map(int,input().split()))
maxNum=max(data)
dp=[0]*(maxNum+1)
for i in data:
    dp[i]=1
answer=[0 for _ in range(maxNum+1)]

for i in sorted(data):
    for j in range(i*2, maxNum+1,i):
        if dp[j]:
            answer[i]+=1
            answer[j]-=1

for i in data:
    print(answer[i], end=' ')