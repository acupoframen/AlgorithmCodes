n=list(input())
left=[]
right=[]
temp=0
answer=0
for i in n:
    if i=='K':
        temp+=1
    else:
        left.append(temp)
temp=0
for i in n[::-1]:
    if i=='K':
        temp+=1
    else:
        right.append(temp)

right.reverse()
l,r=0,len(left)-1
while l<=r:
    answer=max(answer,r-l+1+2*min(left[l],right[r]))
    if left[l]<right[r]:
        l+=1
    else:
        r-=1
print(answer)