n,m=map(int,input().split())
back=0
for _ in range(n): 
    a,b=map(int,input().split())
    if b==1:
        back+=1

answer=((m-1)**back)%1000000007
answer+=((n-back)*(m-1)**(back+1))%1000000007
if back>=1:
    answer+=back*(m-1)**(back-1)%1000000007

print(answer%1000000007)
