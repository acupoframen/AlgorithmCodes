import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    if n%8:
        print("No")
        continue
    n//=8
    n=str(n)
    curr=0
    flag=0
    for i in n:
        if curr<=int(i)<9:
            curr=int(i)
        else:
            flag=1
            break
    if flag:
        print("No")
    else:
        print("Yes")
