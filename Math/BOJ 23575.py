q=int(input())
for _ in range(q):
    a,b=map(int,input().split())
    if a*2<=b and not b%a:
        print(1)
    else:
        print(0)