n,m,k = map(int,input().split())
data=[0]+list(map(int,input().split()))
friends=[i for i in range(n+1)]

def find(a):
    if friends[a]!=a:
        friends[a]=find(friends[a])
    return friends[a]
def union(a,b):
    a=find(a)
    b=find(b)
    if a>b:
        friends[a]=b
    else:
        friends[b]=a

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)
friendcount=[1 for _ in range(n+1)]
dp=[0 for _ in range(k)]
for i in range(1,n+1):
    if i!=friends[i]:
        root=find(i)
        data[root]+=data[i]
        friendcount[root]+=friendcount[i]

for i in range(1,n+1):
    if i!=friends[i]:
        continue
    for j in range(k-1,friendcount[i]-1,-1):
        dp[j]=max(dp[j],dp[j-friendcount[i]]+data[i])

print(max(dp))