from collections import defaultdict
n,m=map(int,input().split())
val=list(map(int,input().split()))
d=defaultdict(int)
for i in range(m):
    a,*b=input().split()
    a=int(a)
    d[a]=0
    for j in range(n):
        if b[j]=='O':
            d[a]+=val[j]
answer=list(d.items())
answer.sort(key=lambda x: (-x[1], x[0]))

print(*answer[0])