n=int(input())
sx,sy,ex,ey=map(int,input().split())
answer=0
minimumVal=1e100
for i in range(1,n+1):
    m=int(input())
    currX=sx
    currY=sy
    value=0
    for _ in range(m):
        x,y=map(int,input().split())
        value+=abs(currX-x)+abs(currY-y)
        currX,currY=x,y
    value+=abs(currX-ex)+abs(currY-ey)
    if minimumVal>value:
        minimumVal=value
        answer=i
print(answer)

