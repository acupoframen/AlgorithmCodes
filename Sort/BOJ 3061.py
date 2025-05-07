import sys
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    data=list(map(int,input().split()))
    answer=0
    for i in range(n-1):
        for j in range(i+1,n):
            if data[i]>data[j]:
                answer+=1  
                data[i],data[j]=data[j],data[i]
    print(answer)