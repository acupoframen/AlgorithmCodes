hp1,hp2=map(int,input().split())
a,b,c,d=map(int,input().split())
n=int(input())
data=list(0 for _ in range(301))
for i in range(n):
    time,skill=input().split()
    time=int(time)
    if skill=='attack':
        if time+5<=300:
            data[time+5]=1
    else:
        for i in range(time,min(time+14,300)):
            data[i]=-1
        if time+15<=3000:
            data[time+15]=2
        
dp=list(list(list([1e10,1e10,1e10] for _ in range(hp2)) for _ in range(hp1)) for _ in range(301))

