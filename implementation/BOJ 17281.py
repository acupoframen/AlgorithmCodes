import sys
from itertools import permutations
input=sys.stdin.readline
maxScore=0
n=int(input())
data=list([1e10]+list(map(int,input().split())) for _ in range(n))
for order in permutations(range(2,10),8):
    order=list(order[:3])+[1]+list(order[3:])
    hitter=0
    score=0
    for i in range(n):
        outCount=0 
        base1=0
        base2=0
        base3=0
        while outCount<3:
            result=data[i][order[hitter]]
            hitter=(hitter+1)%9
            if not result:
                outCount+=1
            elif result==1:
                score+=base3
                base3=base2
                base2=base1
                base1=1
            elif result==2:
                score+=(base3+base2)
                base3=base1
                base2=1
                base1=0
            elif result==3:
                score+=(base1+base2+base3)
                base3=1
                base2=0
                base1=0
            else:
                score+=(base1+base2+base3+1)
                base1=0
                base2=0
                base3=0
    maxScore=max(maxScore,score)
print(maxScore)