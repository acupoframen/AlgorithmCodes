n=int(input())
data=list(map(int,input().split()))
data.sort()
if sum(data)%3:
    print("NO")
    exit(0)
count=sum(data)//3
temp=0
for i in range(n):
    temp+=data[i]//2
if temp>=count:
    print("YES")
else:
    print("NO")