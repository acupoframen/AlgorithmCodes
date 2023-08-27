import sys
input=sys.stdin.readline
def init(node,start,end):
    if start==end:
        tree[node]=array[start]
        return tree[node]
    mid=(start+end)//2
    tree[node]=init(node*2,start,mid)+init(node*2+1,mid+1,end)
    return tree[node]

def sum(node,start,end,left,right):
    if start>right or end<left:
        return 0
    elif left<=start and end<=right:
        return tree[node]
    else:
        mid=(start+end)//2
        return sum(2*node, start, mid, left,right)+sum(2*node+1,mid+1,end,left,right)
    
def update(node,start,end,idx,diff):
    if start>idx or end<idx:
        return
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(2*node,start,mid,idx,diff)
        update(2*node+1,mid+1,end,idx,diff)
    return

n,m,k=map(int,input().split())
array=list()
tree=[0]*(4*n)
for _ in range(n):
    array.append(int(input()))

init(1,0,n-1)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        diff=c-array[b-1]
        array[b-1]=c
        update(1,0,n-1,b-1,diff)
    elif a==2:
        print(sum(1,0,n-1,b-1,c-1))
    