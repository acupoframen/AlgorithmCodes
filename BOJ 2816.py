n=int(input())
data=[input() for _ in range(n)]
answer=""
curr=0
for i in range(1,n):
    if data[i]=='KBS1':
        curr