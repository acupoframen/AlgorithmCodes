n,m=map(int,input().split())
data=list(input() for _ in range(n))
answer=0
data.sort()
for _ in range(m):
    s=input()
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if s<=data[mid]:
            right=mid-1
        else:
            left=mid+1
    l=len(s)
    if left!=n and data[left][:l]==s:
        answer+=1
print(answer)