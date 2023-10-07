t=int(input())
for _ in range(t):
    n=int(input())
    data={}
    for _ in range(n):
        a,b=input().split()
        if b in data:
            data[b]+=1
        else:
            data[b]=1
    answer=1
    for i in data.values():
        answer*=(i+1)
    print(answer-1)