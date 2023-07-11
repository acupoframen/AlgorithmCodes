import sys
input=sys.stdin.readline

line=input()
n=len(line)
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
answer=[1e10 for _ in range(n+1)]
answer[0]=0

for i in range(1,n+1): #하나짜리는 무조건 펠린드롬
    dp[i][i]=1 

for i in range(1,n): #두칸짜리 확인
    if line[i]==line[i-1]:
        dp[i][i+1]=1

for i in range(2,n): #i == 길이
    for j in range(1,n+1-i): # j==시작점. (1이 처음)
        if line[j-1]==line[j+i-1] and dp[j+1][i+j-1]==1:
            dp[j][i+j]=1
for i in range(1,n+1): #시작점부터 dp 확인하면서 화깅
    answer[i]=min(answer[i], answer[i-1]+1)
    for j in range(i+1,n+1):
        if dp[i][j]!=0:
            answer[j]=min(answer[j],answer[i-1]+1)
print(answer[n]-1)