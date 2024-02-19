w,h,k,t=map(int,input().split())
answer=1
for _ in range(k):
    a,b=map(int,input().split())
    left=1 if a-t<=0 else a-t
    top=1 if b-t<=0 else b-t
    right=w if a+t>=w else a+t
    bottom=h if b+t>=h else b+t
    temp=(right-left+1)*(bottom-top+1)
    answer*=temp
    answer=answer%998244353

print(answer)