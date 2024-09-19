n,k,b=map(int,input().split())
data=list(0 for _ in range(n+1))
for _ in range(b):
    num=int(input())
    data[num]=1

count=0
for i in range(1,k+1):
    count+=data[i]
answer=count
for i in range(k+1,n+1):
    count+=data[i]
    count-=data[i-k]
    answer=min(answer,count)
print(answer)