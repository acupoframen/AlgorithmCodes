import sys
input=sys.stdin.readline

n,x=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
answer=[0 for _ in range(n)]
val=0
justfood=0
for i in range(n):
    justfood+=b[i]
    temp=(justfood-a[i])//x
    if temp<0:
        print(-1)
        exit(0)
    val=temp
print(val)