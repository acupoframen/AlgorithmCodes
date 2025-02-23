n=int(input())
male=list(map(int,input().split()))
female=list(map(int,input().split()))
male.sort()
female.sort()
i1=0
i2=n-1
answer=0
while i1<n and 0<=i2:
    if male[i1]<0 and 0<female[i2] and male[i1]+female[i2]<0:
        answer+=1
        i1+=1
        i2-=1
    elif male[i1]<0 and 0<female[i2]:
        i2-=1
    elif 0<male[i1] and female[i2]<0 and male[i1]+female[i2]<0:
        answer+=1
        i1+=1
        i2-=1
    elif 0<male[i1] and female[i2]<0:
        i2-=1
    elif male[i1]>0 and female[i2]>0:
        i2-=1
    elif male[i1]<0 and female[i2]<0:
        i1+=1    

print(answer)