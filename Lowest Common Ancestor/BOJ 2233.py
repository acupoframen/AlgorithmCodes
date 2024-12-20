import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e5))
n=int(input())
numbers=input().strip()
x,y=map(int,input().split())
a,b=0,0
parents=list(0 for _ in range(n+1))
depth=list(0 for _ in range(n+1))
inout=[[0,0] for _ in range(n+1)]
prev,last=0,0
for i in range(1,2*n+1):
    num=numbers[i-1]
    if num=='1':
        inout[prev][1]=i
        prev=parents[prev]
    else:
        last+=1
        parents[last]=prev
        depth[last]=depth[prev]+1
        prev=last
        inout[last][0]=i

for i in range(1,n+1):
    if x in inout[i]:
        a=i
    if y in inout[i]:
        b=i
        
while depth[a]!=depth[b]:
    if depth[a]>depth[b]:
        a=parents[a]
    else:
        b=parents[b]
while a!=b:
    a=parents[a]
    b=parents[b]

print(*inout[a])