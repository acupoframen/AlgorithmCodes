n=int(input())
score=0 #if positive, 1 is winning
onewinning=0
twowinning=0
lasttime=0
for _ in range(n):
    team,time=input().split()
    minute,second=map(int,time.split(":"))
    currenttime=minute*60+second
    if score>0:
        onewinning+=currenttime-lasttime
    elif score<0:
        twowinning+=currenttime-lasttime
    if team=='1':
        score+=1
    else:
        score-=1
    lasttime=currenttime
if score>0:
    onewinning+=48*60-lasttime
elif score<0:
    twowinning+=48*60-lasttime

print("%02d:%02d" %(onewinning//60,onewinning%60))
print("%02d:%02d" %(twowinning//60,twowinning%60))
