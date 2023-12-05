n,m=map(int,input().split())
data=list(map(int,input().split()))
numbers=[0 for i in range(n+1)]
for i in data:
    for j in range(i,n+1,i):
        numbers[j]=1
answer=0
for i in range(1,n+1):
    if numbers[i]==1:
        answer+=i
print(answer)
