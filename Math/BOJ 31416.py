q=int(input())
for _ in range(q):
    a,b,c,d=map(int,input().split())
    answer=0
    timeendb=b*d
    thingsleft=c-timeendb//a
    answer=1e10
    if thingsleft<=0:
        print(timeendb)
        continue
    for i in range(thingsleft+1):
        answer=min(answer,max(timeendb+i*a,(timeendb//a)*a+a*(thingsleft-i)))
    print(answer)