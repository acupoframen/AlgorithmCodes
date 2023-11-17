n,m,r=map(int,input().split())
loc=list(map(int,input().split()))
length=list(map(int,input().split()))
answer=-1
loc.sort()
length.sort()
loclist=[0 for _ in range(40000)]
for i in range(n):
    for j in range(i+1,n):
        loclist[loc[j]-loc[i]]=1
for i in 
