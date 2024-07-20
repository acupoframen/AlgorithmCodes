a,k,m=map(int,input().split())
data=list(map(int,input().split()))
curr=k
for _ in range(m):
    c=int(input())
    if c>0 and curr<=c:
        curr=abs(curr-(c+1))
    elif c<0 and curr>c+a:
        curr=abs(a-curr+1+a+c)
print(curr)