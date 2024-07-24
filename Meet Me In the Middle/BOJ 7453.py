import sys
from collections import defaultdict
input=sys.stdin.readline
n=int(input())
a=list()
b=list()
c=list()
d=list()
for _ in range(n):
    a1,b1,c1,d1=map(int,input().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)
first=defaultdict(int)
for i in range(n):
    for j in range(n):
        ab=a[i]+b[j]
        first[ab]+=1
answer=0
for i in range(n):
    for j in range(n):
        cd=c[i]+d[j]
        if first.get(-cd):
            answer+=first.get(-cd)
print(answer)