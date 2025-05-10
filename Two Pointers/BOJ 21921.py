n,x=map(int,input().split())
data=list(map(int,input().split()))
curr=sum(data[:x])
maxval=sum(data[:x])
count=1
for i in range(x,n):
    curr+=data[i]-data[i-x]
    if curr>maxval:
        maxval=curr
        count=1
    elif curr==maxval:
        count+=1

if maxval==0:
    print("SAD")
    exit(0)
print(maxval)
print(count)