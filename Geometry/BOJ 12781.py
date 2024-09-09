data=list(map(int,input().split()))

def ccw(a,b,c):
    temp=(b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    if temp<0:
        return 1
    elif temp==0:
        return 0
    else:
        return -1

answer=ccw(data[:2],data[2:4],data[4:6])*ccw(data[:2],data[2:4],data[6:8])
if answer<0:
    print(1)
else:
    print(0)