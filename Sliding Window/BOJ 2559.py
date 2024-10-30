n,k=map(int,input().split())
data=list(map(int,input().split()))
answer=sum(data[:k])
curr=sum(data[:k])
for i in range(n-k):
    curr-=data[i]
    curr+=data[k+i]
    answer=max(curr,answer)
print(answer)