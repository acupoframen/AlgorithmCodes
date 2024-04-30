x,y=map(int,input().split())
goal=y-x
curr=1
val=0
answer=0
while val<goal:
    if val>=goal:
        break
    if val+curr>=goal:
        answer+=1
        break
    else:
        val+= 2*curr
        curr+=1
        answer+=2
print(answer)