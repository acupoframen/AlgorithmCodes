n,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
answer=0
left=0
right=n-1
while left<right:
    if data[left]+data[right]<=k:
        answer+=1
        left+=1
        right-=1
    else:
        right-=1
print(answer)