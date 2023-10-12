n=int(input())
for _ in range(n):
    data=list(input().split())
    print(*data[2:],*data[0:2])