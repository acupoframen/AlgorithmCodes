from math import gcd
from collections import defaultdict
n=int(input())
data=list(list(map(int,input().split())) for _ in range(n))
posangle=defaultdict(float) #x>0
negangle=defaultdict(float) #x<0
updown=[0,0] #up,down
for i in range(n):
    x,y=data[i]
    if x==0:
        if y>0:
            updown[0]=1
        else:
            updown[1]=1
        continue
    x,y=x//gcd(x,y),y//gcd(x,y)
    if x>0:
        posangle[y/x]=1
    else:
        negangle[y/x]=1
print(sum(updown)+len(posangle)+len(negangle))