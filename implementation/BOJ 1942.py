def realtime(h,m,s):
    return 3600*h+60*m+s
def tentime(val):
    return 10000*(val//3600)+100*((val%3600)//60)+val%60
for i in range(3):
    a,b=input().split()
    answer=0
    dataa=list(map(int,a.split(":")))
    datab=list(map(int,b.split(":")))
    vala=realtime(*dataa)
    valb=realtime(*datab)
    if vala>valb:
        valb+=realtime(24,0,0)
    for i in range(vala,valb+1):
        if tentime(i)%3==0:
            answer+=1
    print(answer)