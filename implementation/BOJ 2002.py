import sys
from collections import defaultdict
input=sys.stdin.readline
n=int(input())
out=list()
data=defaultdict(int)
for i in range(n):
    data[input().strip()]=i
for _ in range(n):
    out.append(input().strip())
answer=0
for i in range(n-1):
    for j in range(i+1,n):
        if data[out[i]]>data[out[j]]:
            answer+=1
            break
print(answer)