t=int(input())
def binaryfind(num,small):
    left=0
    right=len(small)-1
    while left<=right:
        mid=(left+right)//2
        if num>small[mid]:
            left=mid+1
        else:
            right=mid-1
    return left

for _ in range(t):
    a,b=map(int,input().split())
    data=list(map(int,input().split()))
    small=list(map(int,input().split()))
    data.sort()
    small.sort()
    answer=0
    for i in data:
        answer+=binaryfind(i,small)
    print(answer)