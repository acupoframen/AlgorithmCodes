n=int(input())
answer=[0 for _ in range(n+1)]
data=list(map(int,input().split()))
for i in range(1,n+1):
    answer[data[i-1]]=i
for i in range(1,n+1):
    print(i-answer[i])
