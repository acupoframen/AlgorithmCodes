n,k=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
answer=0
def check(x):
    global answer,n
    if x<=n:
        answer=max(x,answer)
        for i in data:
            check(x*10+i)
for i in data:
    check(i)
print(answer)