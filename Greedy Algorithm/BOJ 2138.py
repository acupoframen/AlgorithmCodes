n=int(input())
data=list(map(int,input()))
goal=list(map(int,input()))
tempdata=data[:]
count=0
for i in range(1,n):
    if data[i-1]!=goal[i-1]:
        count+=1
        data[i]=int(not data[i])
        data[i-1]=int(not data[i-1])
        if i!=n-1:
            data[i+1]=int(not data[i+1])
if data==goal:
    print(count)
    exit()
cnt = 1

tempdata[0] = not tempdata[0]
tempdata[1] = not tempdata[1]

for i in range(1,n):
    if tempdata[i-1]!=goal[i-1]:
        cnt+=1
        tempdata[i]=int(not tempdata[i])
        tempdata[i-1] = int(not tempdata[i-1])
        if i!=n-1:
            tempdata[i+1]=int(not tempdata[i+1])
if tempdata==goal:
    print(cnt)
    exit(0)
print(-1)