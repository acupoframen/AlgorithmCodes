import sys
input=sys.stdin.readline
n,m=map(int,input().split())
data={}
for i in range(n):
    name=input().strip()
    data[name]=i+1
    data[str(i+1)]=name

for _ in range(m):
    name=input().strip()
    print(data[name])