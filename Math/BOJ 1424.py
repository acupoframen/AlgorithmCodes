n=int(input())
l=int(input())
c=int(input())

musiccount=0
for i in range(1,n+1):
    if i%13==0:
        continue
    if i*l+i-1>c:
        break
    musiccount=i
answer=0
nsave=n
while n>nsave%musiccount:
    n-=musiccount
    answer+=1
if n==0:
    pass
elif n%13==0:
    if musiccount-n==1:
        answer+=2
    elif musiccount-n==2:
        if (musiccount-1)%13==0:
            answer+=2
        else:
            answer+=1
    else:
        answer+=1
    
elif n!=0:
    answer+=1

print(answer)