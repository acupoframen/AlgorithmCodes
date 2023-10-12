n=int(input())
data=list(map(int,input().split()))
data.sort()
if n==1:
    print(data[0])
    exit(0)
elif n==2:
    print(data[1]*2)
    exit(0)
if n%2:
    print(data[n//2]+sum(data[n//2+1:])*(2))
else:
    print(sum(data[n//2:])*2)