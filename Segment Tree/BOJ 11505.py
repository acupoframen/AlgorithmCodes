import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
data=[]
tree=[1 for  _ in range(n*4)]
def init(node,start,end):
    if start==end:
        tree[node]=data[start]
        return tree[node]
    else:
        tree[node]=(init(node*2,start,(start+end)//2)*init(node*2+1,(start+end)//2+1,end))%1000000007
        return tree[node]%1000000007
    
def calc(node,start,end,left,right):
    if left>end or right<start:
        return 1
    if left<=start and end<=right:
        return tree[node]
    return calc(node*2,start,(start+end)//2,left,right)*calc(node*2+1,(start+end)//2+1,end,left,right)%1000000007


def update(node,start,end,index,diff):
    if index<start or index>end:
        return tree[node]
    if start!=end:
        tree[node]=(update(node*2,start,(start+end)//2,index,diff)*update(node*2+1,(start+end)//2+1,end,index,diff))%1000000007
        return tree[node]
    else:
        tree[node]=diff%1000000007
        return tree[node]

for _ in range(n):
    data.append(int(input()))

init(1,0,n-1)
for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(1,0,n-1,b-1,c)
        data[b-1]=c
    else:
        print(calc(1,0,n-1,b-1,c-1))