s=map(int,input().split())
data=list(map(int,input().split()))
n=int(input())
data.sort()
numbers=[0 for _ in range(1001)]
for i in data:
    numbers[i]=1
leftcount=0
rightcount=0
for i in range(n,0,-1):
    if numbers[i]==1:
        break
    else:
        leftcount+=1
for i in range(n,1001,1):
    if numbers[i]==1:
        break
    else:
        rightcount+=1
if leftcount==0 or rightcount==0:
    print(0)
    exit(0)
leftcount-=1
rightcount-=1
print(leftcount*rightcount+leftcount+rightcount)