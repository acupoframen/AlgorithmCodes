n=int(input())
data=list(int(input()) for _ in range(n))

if n==0:
    print(0)
    exit(0)
data.sort()
fifteen=int(0.15*n+0.5)
print(int(sum(data[fifteen:n-fifteen])/int(n-fifteen*2)+0.5))