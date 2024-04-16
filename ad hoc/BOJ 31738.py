n,m=map(int,input().split())
temp=1
if n>=m:
    print(0)
    exit(0)
for i in range(1,n+1):
    temp*=i
    temp%=m

print(temp)