n,m,x=map(int,input().split()) #사람, 상품 수, 자금
data=list(map(int,input().split()))
answer=[0 for _ in range(m)]
a,b=0,n
people=n
for i in range(m-1):
    temp=0
    if b==0:
        break
    while a<=b:
        mid=(a+b)//2
        if data[i]*mid+data[-1]*(people-mid)>x:
            b=mid-1
        else:
            a=mid+1  
            temp=mid
    answer[i]=temp
    a=0
    b=people-temp
    x-=temp*data[i]
    people-=temp
answer[-1]=people
print(*answer)