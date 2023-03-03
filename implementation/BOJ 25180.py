n=int(input())
data=[0]+[1]*9+[2,3]*5+[3]*8
if n<28:
    print(data[n])
else:
    answer=0
    while n>=28:
        n-=18
        answer+=2
    print(data[n]+answer)
