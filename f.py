import sys
import math
input=sys.stdin.readline
n,m=map(int,input().split())
data=list(map(int,input().split()))
fpoint=0
lpoint=m-1
numbers=[0]*(int(4*1e6))
limit=math.ceil(9*m/10)
for i in range(lpoint+1):
    numbers[data[i]]+=1
for i in range(n-m+1):
    if i:
        numbers[data[fpoint]]-=1
        fpoint+=1
        lpoint+=1
        numbers[data[lpoint]]+=1
    if numbers[data[fpoint]]>=limit or numbers[data[lpoint]]>=limit:
        print("YES")
        exit(0)
    if lpoint>=n:
        break
print("NO")