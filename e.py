import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    while n>0:
        m+=1
        n//=2
    print(m)