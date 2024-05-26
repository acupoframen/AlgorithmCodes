a=int(input())
m,n=map(int,input().split())
if m>n:
    n,m=m,n

answer=max(m,n/a)
answer=min((m/a)*2,answer)
print(answer)