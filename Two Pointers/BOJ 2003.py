n,m=map(int,input().split())
data=list(map(int,input().split()))
l,r=0,1
answer=0
curr=data[0]
if curr==m:
    answer+=1
while True:
    if l==r==n:
        break
    if curr<m and r<n:
        curr+=data[r]
        r+=1
    else:
        curr-=data[l]
        l+=1
    if curr==m:
        answer+=1

print(answer)