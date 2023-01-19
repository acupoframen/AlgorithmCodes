n,m=map(int,input().split())
data=list(map(int,input().split()))
answer=sum(data[0:m])
comparison=sum(data[0:m])
for i in range(n-m):
    comparison=comparison-data[i]+data[i+m]
    answer=max(answer,comparison)
print(answer)