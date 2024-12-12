while True:
    n,m=map(int,input().split())
    data=set()
    if (n,m)==(0,0):
        break
    for i in range(n):
        data.add(int(input()))
    answer=0
    for i in range(m):
        if int(input()) in data:
            answer+=1
    print(answer)