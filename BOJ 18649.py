import sys
n,k,m=map(int,input().split())
sys.stdout.flush()
for _ in range(m):
    for i in range(1,k+1):
        print(i, end=" ")
    print()
    sys.stdout.flush()
    for i in range(1,n-k+1):
        r=input()
    sys.stdout.flush()