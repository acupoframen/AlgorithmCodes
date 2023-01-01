n,k=map(int,input().split())
coindata=[]
for _ in range(n):
    coindata.append(int(input()))
coindata.sort()
values=[0 for _ in range(k+1)]
values[0]=1
for i in coindata:
    for j in range(1,k+1):
        if j-i>=0:
            values[j]+=values[j-i]
print(values[k])
