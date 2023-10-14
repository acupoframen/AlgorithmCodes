a,b=map(int,input().split())
time=a*60+b-45
if time<0:
    print(23,60+time)
else:
    print(time//60,time%60)