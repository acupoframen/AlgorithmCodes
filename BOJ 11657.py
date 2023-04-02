import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data=[]
for _ in range(m):
    data.append(list(map(int,input().split())))
dist=[1e10]*(n+1)
