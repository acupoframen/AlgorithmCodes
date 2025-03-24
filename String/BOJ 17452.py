n=int(input())
data=list(input() for _ in range(n))
left=list(1e10 for _ in range(26))
right=list(1e10 for _ in range(26))
answer=1e10
for i in data:
    templeft=[1e10 for _ in range(26)]
    tempright=[1e10 for _ in range(26)]
    leng=len(i)
    for j in range(leng):
        k=leng-j-1
        templeft[ord(i[j])-ord('a')]=min(templeft[ord(i[j])-ord('a')],j)
        tempright[ord(i[j])-ord('a')]=min(tempright[ord(i[j])- ord('a')],k)
    for j in range(26):
        if templeft[j]!=1e10 and right[j]!=1e10:
            answer=min(templeft[j]+right[j],answer)
        if tempright[j]!=1e10 and left[j]!=1e10:
            answer=min(tempright[j]+left[j],answer)
        left[j]=min(left[j],templeft[j])
        right[j]=min(right[j],tempright[j])
if answer==1e10:
    print(-1)
else:
    print(answer)
