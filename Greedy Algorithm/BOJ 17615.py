n=int(input())
data=list(input())

firstr=-1
firstb=-1
lastr=n-1
lastb=n-1

for i in range(n):
    if data[i]=='R':
        lastr=i
        if firstr==-1:
            firstr=i
    else:
        lastb=i
        if firstb==-1:
            firstb=i

if firstr==-1 or firstb==-1:
    print(0)
    exit(0)
answer=1e10
answer=min(data[firstb:].count("R"),data[:lastb].count("R"))
answer=min(answer,data[firstr:].count("B"),data[:lastr].count("B"))
print(answer)