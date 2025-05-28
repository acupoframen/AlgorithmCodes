n=int(input())
data=list(list(input()) for _ in range(n))
for i in range(n):
    data[i][0]=data[i][0].upper()
    print(*data[i],sep="")