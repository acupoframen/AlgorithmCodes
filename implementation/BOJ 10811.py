n,m=map(int,input().split())
data=list(i for i in range(n+1))
for _ in range(m):
    a,b=map(int,input().split())
    data=data[:a]+data[a:b+1][::-1]+data[b+1:]

print(*data[1:])