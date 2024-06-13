n=int(input())
data=[0]+list(map(int,input().split()))
rank="0"+input()
answer=0
money=[0 for _ in range(n+1)]
for i in range(1,n+1):
    temp=0
    if rank[i]=='B':
        temp=data[1]-1
    elif rank[i]=='S':
        temp=data[2]-1
    elif rank[i]=='G':
        temp=data[3]-1
    elif rank[i]=='P':
        temp=data[4]-1
    else:
        temp=data[4]
    if rank[i]=='D':
        money[i]=data[4]
    else:
        money[i]=temp-money[i-1]
print(sum(money))