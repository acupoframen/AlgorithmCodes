import sys
input=sys.stdin.readline
n,m=map(int,input().split())
mintree=[1e12 for _ in range(300000)]
maxtree=[0 for _ in range(300000)]

data=[int(input()) for _ in range(n)]

def mininit(node,start,end):
    if start==end:
        mintree[node]=data[start]
    else:
        mid=(start+end)//2
        mintree[node]=min(mininit(node*2,start,mid),mininit(node*2+1,mid+1,end))
    return mintree[node]

def mincheck(node,start,end,left,right):
    if left>end or right<start:
        return 1e12
    if left<=start and end<=right:
        return mintree[node]
    mid=(start+end)//2
    return min(mincheck(node*2,start,mid,left,right),mincheck(node*2+1,mid+1,end,left,right))

def maxinit(node,start,end):
    if start==end:
        maxtree[node]=data[start]
    else:
        mid=(start+end)//2
        maxtree[node]=max(maxinit(node*2,start,mid),maxinit(node*2+1,mid+1,end))
    return maxtree[node]

def maxcheck(node,start,end,left,right):
    if left>end or right<start:
        return -1
    if left<=start and right>=end:
        return maxtree[node]
    mid=(start+end)//2
    return max(maxcheck(node*2,start,mid,left,right),maxcheck(node*2+1,mid+1,end,left,right))

mininit(1,0,n-1)
maxinit(1,0,n-1)

for _ in range(m):
    s,e=map(int,input().split())
    print(mincheck(1,0,n-1,s-1,e-1), maxcheck(1,0,n-1,s-1,e-1))
