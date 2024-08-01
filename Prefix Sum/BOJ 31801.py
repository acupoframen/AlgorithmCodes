import sys
input=sys.stdin.readline
t=int(input())
data=[0 for _ in range(int(1e6)+1)]
for i in range(100,int(1e6)+1):
    n=str(i)
    up=1
    for j in range(1,len(n)):
        if j==1 and n[0]>=n[1]:
            up=1
            break
        if n[j]==n[j-1]:
            up=1
            break
        elif not up and n[j-1]<n[j]:
            up=1
            break
        elif up and n[j-1]>n[j]:
            up=0
    if not up:
        data[i]=data[i-1]+1
    else:
        data[i]=data[i-1]

for _ in range(t):
    a,b=map(int,input().split())
    print(data[b]-data[a-1])