import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
data=[0]+list(int(input()) for _ in range(n))
tree=[0 for _ in range(int(3*1e5))]

def maketree(node,start,end): # putting smallest index of the range
    if start==end:
        tree[node]=start
        return tree[node]
    mid=(start+end)//2
    a=maketree(node*2,start,mid)
    b=maketree(node*2+1,mid+1,end)
    if data[a]<data[b]:
        tree[node]=a
    else:
        tree[node]=b    
    return tree[node]

def minfind(node, start, end, left, right): ##if in range, choose the index with smallest value 
    if right<start or end<left:
        return -1e10 
    elif left<=start and end<=right:
        return tree[node]
    mid = (start+end)//2
    a= minfind(node*2,start,mid,left,right)
    b= minfind(node*2+1,mid+1,end,left,right)
    if a==-1e10:
        return b
    if b==-1e10:
        return a
    else:
        if data[a]<data[b]:
            return a
        else:
            return b

def solve(left,right): #choosing the largest area
    if left==right:
        return data[right]
    minval=minfind(1,1,n,left,right)
    area=data[minval]*(right-left+1)
    if left+1<=minval:
        area1=solve(left,minval-1)
        area=max(area,area1)
    if minval+1<=right:
        area1=solve(minval+1,right)
        area=max(area,area1)
    return area
maketree(1,1,n)
print(solve(1,n))