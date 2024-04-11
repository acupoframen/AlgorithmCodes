import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    data=[]
    for i in range(n):
        a,b=map(int,input().split())
        data.append([a,b])
    data.sort()
    a,b=data[0]
    answer=1
    for i in range(1,n):
        if b>data[i][1]:
            answer+=1
            b=data[i][1]
    print(answer)