x1,y1,x2,y2=map(int,input().split())
x3,y3,x4,y4=map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    return (x2-x1)*(y3-y2)-(x3-x2)*(y2-y1)

answer1=ccw(x1,y1,x2,y2,x3,y3)
answer2=ccw(x1,y1,x2,y2,x4,y4)
answer3=ccw(x3,y3,x4,y4,x1,y1)
answer4=ccw(x3,y3,x4,y4,x2,y2)

if answer1==answer2==answer3==answer4==0:
    if max(x1,x2)<min(x3,x4):
        print(0)
    elif max(x3,x4)<min(x1,x2):
        print(0)
    elif max(y1,y2)<min(y3,y4):
        print(0)
    elif max(y3,y4)<min(y1,y2):
        print(0)
    else:
        print(1)

elif answer1*answer2<=0 and answer3*answer4<=0:
    print(1)
else:
    print(0)