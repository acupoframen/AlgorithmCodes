n=int(input())
data=list(list(0 for _ in range(100)) for _ in range(100))
for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            data[i][j]=1
answer=0
for i in range(100):
    answer+=sum(data[i])
print(answer)