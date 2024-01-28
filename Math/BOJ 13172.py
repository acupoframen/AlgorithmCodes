m=int(input())
answer=0
mod=1000000007
def calc(n,s):
    if s==1:
        return n%mod
    elif s%2:
        return n*calc(n,s-1)%mod
    else:
        temp=calc(n,s//2)
        return (temp*temp)%mod
for _ in range(m):
    n,s=map(int,input().split())
    answer+= s*calc(n,mod-2)%mod

print(answer%mod)