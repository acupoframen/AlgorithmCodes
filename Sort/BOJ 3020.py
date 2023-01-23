import sys
input=sys.stdin.readline

def binary(h,arr):
    l,r= 0, len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]<=h:
            l=mid+1
        else:
            r=mid-1
    return l

n,h=map(int,input().split())
down,up=[],[]
for i in range(n):
    if i%2:
        up.append(int(input()))
    else:
        down.append(int(input()))
down.sort()
up.sort()

answer=[]
for i in range(h):
    answer.append(n-binary(i,down)-binary(h-i-1,up))
answer.sort()
print(answer)
print(answer[0],answer.count(answer[0]))