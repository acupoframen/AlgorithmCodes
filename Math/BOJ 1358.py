w,h,x,y,p=map(int,input().split())
data=list(list(map(int,input().split())) for _ in range(p))
r=h//2
answer=0
for i in range(p):
    a,b=data[i]
    if (a-x)**2+(b-y-r)**2<=r**2 or (a-x-w)**2+(b-y-r)**2<=r**2:
        answer+=1
    elif x<=a<=x+w and y<=b<=y+h:
        answer+=1
print(answer)