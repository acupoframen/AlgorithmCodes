n,x=map(int,input().split())
data=sorted(list(map(int,input().split())))
answer=0
for i in range(n-1,-1,-1):
    if data[i]==x:
        data.pop()
        answer+=1
    else:
        break
start,end=0,len(data)-1
rest=0
while start<=end:
    if start==end:
        rest+=1
        break
    if 2*(data[start]+data[end])>=x:
        start+=1
        end-=1
        answer+=1
    else:
        rest+=1
        start+=1
print(answer+rest//3)