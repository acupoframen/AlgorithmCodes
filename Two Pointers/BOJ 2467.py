n=int(input())
data=list(map(int,input().split()))
data.sort()
a=0
b=len(data)-1
answer=1e10
answerset=[]
while a!=b:
    if data[a]+data[b]<0:
        if abs(answer)>abs(data[a]+data[b]):
            answer=data[a]+data[b]
            answerset=[data[a],data[b]]
        a+=1
    elif data[a]+data[b]>0:
        if abs(answer)>abs(data[a]+data[b]):
            answer=data[a]+data[b]
            answerset=[data[a],data[b]]
        b-=1
    else:
        print(data[a],data[b])
        exit(0)
print(*answerset)