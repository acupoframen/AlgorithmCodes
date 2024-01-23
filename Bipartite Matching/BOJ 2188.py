import sys
input=sys.stdin.readline

def dfs(i):
    if i==1e10 or temp[i]:
        return False
    temp[i]=1
    for j in data[i]:
        if house[j]==1e10 or dfs(house[j]):
            house[j]=i
            return True
    return False
n,m=map(int,input().split())
data=[0]+list(list(map(int,input().strip().split()[1:])) for _ in range(n))
house=[1e10 for _ in range(m+1)]

for i in range(1,n+1):
    temp= [ 0 for _ in range(n+1)]
    dfs(i)
print(m-house.count(1e10)+1)