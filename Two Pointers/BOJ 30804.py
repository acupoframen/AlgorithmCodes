n=int(input())
data=list(map(int,input().split()))
answer=0
curr=[0 for _ in range(10)]
left=0
right=0
while right<n:
    fruit=data[right]
    curr[fruit]+=1
    while curr.count(0)==7:
        curr[data[left]]-=1
        left+=1
    answer=max(answer,right-left+1)
    right+=1
print(answer)