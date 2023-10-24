n,m=map(int,input().split())
answer=0
data=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if data[i]+data[j]+data[k]<=m:
                answer=max(answer,data[i]+data[j]+data[k])

print(answer)