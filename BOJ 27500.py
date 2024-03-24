hp1,hp2=map(int,input().split())
a,b,c,d=map(int,input().split())
k=int(input())
data=[0 for _ in range(301)]
i=0
while i<301:
    a,b=input().split()
    if b=='attack':
        i+=4
        if data[i]<=300:
            data[i]=c
        i+=1
    elif b=='riposte':
        for k in range(14):
            if i+k<=300:
                data[i+k]=-1
            else:
                break
        i+=14
        if data[i]<=300:
            data[i]=d
        i+=1
dp=list(list(list([0,0,0] for _ in range(hp2)) for _ in range(hp1)) for _ in range(301))

for i in range(301):
    if data