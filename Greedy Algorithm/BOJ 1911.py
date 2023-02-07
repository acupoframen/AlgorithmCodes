import sys
input=sys.stdin.readline
n,l=map(int,input().split())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))

data.sort()
woodStart=0
answer=0
for i in range(n):
    holeStart,holeEnd=data[i]
    woodStart=max(woodStart,holeStart)
    diff=holeEnd-woodStart
    count=(diff+l-1)//l
    answer+=count
    woodStart+=count*l
    
print(answer)