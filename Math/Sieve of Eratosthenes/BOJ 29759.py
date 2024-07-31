n=int(input())
sieve=[1 for _ in range(1000001)]
sieve[1]=0
data=list(list(map(int,input().split())) for _ in range(n**2))

for i in range(2,1001):
    if not sieve[i]:
        continue
    for j in range(2*i,1000001,i):
        sieve[j]=0

for i in range(n**2):
    for j in range(n**2):
        sieve[data[i][j]]=0
curr=1000000
for i in range(n**2):
    for j in range(n**2):
        if data[i][j]==0:
            while not sieve[curr]:
                curr-=1
            data[i][j]=curr
            curr-=1

for i in range(n**2):
    print(*data[i])