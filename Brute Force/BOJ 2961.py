from itertools import combinations

n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
answer=1e10
for i in range(1,n+1):
    for j in combinations(data,i):
        s=1
        b=0
        for k in j:
            s*=k[0]
            b+=k[1]
        answer=min(answer,(abs(s-b)))

print(answer)