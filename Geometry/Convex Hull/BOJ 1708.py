n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
data.sort(key=lambda x:(x[0],x[1]))

def ccw(p1,p2,p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

def convex():
    lower=[]
    for i in data:
        while len(lower)>=2 and ccw(lower[-2],lower[-1],i)<=0:
            lower.pop()
        lower.append(i)
    upper=[]
    for i in reversed(data):
        while len(upper)>=2 and ccw(upper[-2],upper[-1],i)<=0:
            upper.pop()
        upper.append(i)
    return len(lower+upper)

print(convex()-2)