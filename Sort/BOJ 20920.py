import sys
input=sys.stdin.readline
from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(int)
for _ in range(n):
    temp=input().strip()
    if len(temp)>=m:
        d[temp]+=1
answer=[]
for i in d:
    answer.append([d[i],len(i),i])
answer.sort(key=lambda x:(-x[0],-x[1],x[2]))
for i in answer:
    print(i[2])