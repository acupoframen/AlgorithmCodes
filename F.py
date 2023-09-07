n,m=map(int,input().split())
backdata=[]
for _ in range(n):
    a,b=map(int,input().split())
    if a>b:
        backdata.append([a,b])

if len(backdata)==0:
    print(m)
    exit(0)

if len(backdata)==1:
    print(m+2*(backdata[0][0]-backdata[0][1]))
    exit(0)
    
backdata.sort(key=lambda x:(x[1],x[0]))
left=backdata[0][1]
right=backdata[0][0]
curr=right
answer=right
for i in range(1,len(backdata)):
    if i==len(backdata)-1:
        answer+=(curr-left)
        answer+=(m-left)
    if backdata[i][1]<right:
        answer+=(backdata[i][0]-curr)
        curr=backdata[i][0]
        right=backdata[i][0]
    else:
        answer+=(curr-left)
        answer+=(backdata[i][0]-left)
        curr=backdata[i][0]
        right=backdata[i][0]
        left=backdata[i][1]

print(answer)