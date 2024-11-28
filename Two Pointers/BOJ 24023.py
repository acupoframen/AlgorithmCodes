n,k=map(int,input().split())
data=list(map(int,input().split()))
left=0
right=0
curr=0
for i in range(n):
    curr=curr|data[i]
    if curr==k:
        print(left+1,right+1)
        exit(0)
    elif k|curr>k:
        left=i+1
        right=i+1
        curr=0
    else:
        right+=1

print(-1)