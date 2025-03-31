n,l,r,w=map(int,input().split())
data=list(map(int, input().split()))
answer=0
for i in range(1,1<<n):
    temp=[]
    for j in range(n):
        if i & (1 << j):
            temp.append(data[j])
    if len(temp)<2:
        continue
    total=sum(temp)
    diff=max(temp)-min(temp)
    if l<=total<=r and diff>=w:
        answer+=1
print(answer)