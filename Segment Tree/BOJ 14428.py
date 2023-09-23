import sys
input=sys.stdin.readline

n=int(input())
data=[]
tree=[0]*(n*4)
array=list(map(int,input().split()))
for i in range(n):
    data.append([array[i],i+1])

def init(start, end, index):
    if start==end:
        tree[index]=data[start]
    else:
        mid=(start+end)//2
        tree[index]=min(init(start,mid,index*2), init(mid +1 , end, index*2+1))
    return tree[index]


def update (start,end,index,left,right):
    if start>left or end<left:
        return
    if start==end:
        tree[index]=right
        return
    mid=(start+end)//2
    update(start,mid,index*2,left,right)
    update(mid+1,end,index*2+1,left,right)
    tree[index]=min(tree[index*2], tree[index*2+1])


def find(start,end,index,left,right):
    if start>right or end<left:
        return [1e11, 1e11]
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2

    return min(find(start,mid,index*2,left,right), find(mid+1,end,index*2+1,left,right))

init(0,n-1,1)
q=int(input())
for _ in range(q):
    a,b,c=map(int,input().split())
    if a==1:
        data[b-1][0]=c
        update(0,n-1,1,b-1,data[b-1])
    else:
        print(find(0,n-1,1,b-1,c-1)[1])