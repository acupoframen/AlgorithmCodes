from itertools import combinations
n,c=map(int,input().split())
data=list(map(int,input().split()))
left=data[:n//2]
right=data[n//2:]
leftsum=[]
rightsum=[]
for i in range(len(left)+1):
    a=combinations(left,i)
    for j in a:
        leftsum.append(sum(j))

for i in range(len(right)+1):
    b=combinations(right,i)
    for j in b:
        rightsum.append(sum(j))

leftsum.sort()
answer=0
for i in rightsum:
    if i>c:
        continue
    start=0
    end=len(leftsum)-1
    while start<=end:
        mid=(start+end)//2
        if leftsum[mid]+i>c:
            end=mid-1
        else:
            start=mid+1
    answer+=end+1
print(answer)