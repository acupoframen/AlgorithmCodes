n,k=map(int,input().split())
data=list(map(int,input().split()))
answer=0
left=0 
right=0
numbers=list(0 for _ in range(int(1e5)+1))
while right<n:
    if numbers[data[right]]>=k:
        numbers[data[left]]-=1
        left+=1
    else:
        numbers[data[right]]+=1
        right+=1
        answer=max(answer,right-left)

print(answer)