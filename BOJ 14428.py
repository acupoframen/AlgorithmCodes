import sys
input=sys.stdin.readline
n=int(input())
data=[0]+list(map(int,input().split()))
m=int(input())
tree=[[] for _ in range(4*n)]
def init(node,start,end):
    if start==end:
        tree[node]=[data[start],start]
        return tree[node]
    mid=(start+end)//2
    val1,index1=init(node*2,start,end)
    val2,index2=init(node*2,mid+1,end,2*idx+1)
    if val1<val2:
        tree[node]=(val1,index1)
    elif val1>val2:
        tree[node]=(val2,index2)
    else:
        index1=min(index1,index2)
        tree[node]=(val1,index1)
    return tree[node]


def find(node,start,end,left,right):
    if start>right or end<left:
        return [int(1e10),1000001]
    elif left<=start and end<=right:
        return tree[node]
    else:
        mid=(start+end)//2
        return sum(2*node, start, mid, left,right)+sum(2*node+1,mid+1,end,left,right)
    
def update(node,start,end,idx,diff):
    if start>idx or end<idx:
        
    tree[node]+=diff
    if start!=end:
        mid=(start+end)//2
        update(2*node,start,mid,idx,diff)
        update(2*node+1,mid+1,end,idx,diff)
    return


for _ in range(m):
    a,b,c=map(int,input().split())
    if a==1:
    
    else:
