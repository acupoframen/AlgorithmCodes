t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split())
    n=int(input())
    data=[]
    for _ in range(n):
        data.append(list(map(int,input().split())))
    answer=0
    for x,y,r in data:
        d1 = (((x1-x)**2) + ((y1-y)**2))**0.5
        d2 = (((x2-x)**2)+((y2 - y)**2)) ** 0.5
        if d1<r<d2 or d2<r<d1:  
            answer += 1
    print(answer)