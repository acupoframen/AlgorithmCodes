n,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
answer=[]
left=0
right=n-1
for i in range(k):
    if not i%2:
        answer.append(data[right])
        right-=1
    else:
        answer.append(data[left])
        left+=1
    
val=answer[0]
for i in range(1,k):
    if answer[i]-answer[i-1]>0:
        val+=answer[i]-answer[i-1]

print(val)