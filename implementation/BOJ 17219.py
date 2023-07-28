import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data={}
for _ in range(n):
    a,b=input().strip().split()
    data[a]=b
for _ in range(m):
    print(data[input().strip()])