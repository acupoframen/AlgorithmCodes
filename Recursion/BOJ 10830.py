def solve(num):
    answer=[[0]*n for _ in range(n)]
    if num==1:
        for i in range(n):
            for j in range(n):
                answer[i][j]=data[i][j]%1000
    elif num%2:
        half=solve(num//2)
        temp=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[i][j]=sum(half[i][t]*half[t][j] for t in range(n)) %1000
        for i in range(n):
            for j in range(n):
                answer[i][j]+=sum(temp[i][t]*data[t][j] for t in range(n)) % 1000
    else:
        half=solve(num//2)
        for i in range(n):
            for j in range(n):
                answer[i][j]=sum(half[i][t]*half[t][j] for t in range(n))%1000
    return answer
n,b=map(int,input().split())
data=[list(map(int,input().split())) for _ in range(n)]
answer=solve(b)
for i in answer:
    print(*i)