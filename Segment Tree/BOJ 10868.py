n,m=map(int,input().split())
data=list(int(input()) for _ in range(n))

def init(start,end,index):
    if start==end:
        tree[index]=[data[start],data[start]]
        return tree[index]
    mid=(start+end)//2
    left=init(start,mid,index*2)
    right=init(mid+1,end,index*2+1)
    tree[index]=[min(left[0],right[0]),max(left[1],right[1])]
    return tree[index]

def find(start,end,index,left,right):
    if start>right or end<left:
        return [1e9+1,0]
    if left<=start and right>=end:
        return tree[index]
    mid=(start+end)//2
    l=find(start,mid,index*2,left,right)
    r=find(mid+1,end,index*2+1,left,right)
    return [min(l[0],r[0]),max(l[1],r[1])]

tree=list(0 for _ in range(n*4))
answer=[]
init(0,n-1,1)

for _ in range(m):
    a,b=map(int,input().split())
    print(find(0,n-1,1,a-1,b-1)[0])