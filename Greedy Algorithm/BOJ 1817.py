n,m=map(int,input().split())
if not n:
    print(0)
    exit(0)
data=list(map(int,input().split()))
currweight=0
curr=1
for i in range(n):
    if currweight+data[i]<=m:
        currweight+=data[i]
    else:
        curr+=1
        currweight=data[i]
print(curr)