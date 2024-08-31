t=int(input())
data=list(list(0 for _ in range(10)) for _ in range(1001))
data[1]=[1 for _ in range(10)]
for i in range(2,1001):
    for j in range(10):
        for k in range(j+1):
            data[i][j]+=data[i-1][k]
for _ in range(t):
    n=int(input())
    print(sum(data[n]))