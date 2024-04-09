t=int(input())
for _ in range(t):
    n=int(input())
    answer=1e10
    effi=1e10
    for i in range(n):
        a,b=map(int,input().split())
        if b/a<effi:
            answer=b
            effi=b/a
        elif b/a==effi:
            answer=min(b,answer)
    print(answer)