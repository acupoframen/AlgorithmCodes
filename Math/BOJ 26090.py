n=int(input())
prime=[0,0]+[1]*(int(1e6))
for i in range(2,int(1e3)+1):
    if prime[i]==1:
        for j in range(2*i,int(1e6)+1,i):
            prime[j]=0
data=list(map(int,input().split()))
answer=0
for i in range(2,n+1):
    if prime[i]==0:
        continue
    for j in range(n-i+1):
        if prime[sum(data[j:j+i])]==1:
            
            answer+=1

print(answer)