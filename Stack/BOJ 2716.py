n=int(input())
for i in range(n):
    s=list(input())
    maxtemp=0
    temp=0
    for j in s:
        if j=="[":
            temp+=1
            maxtemp=max(maxtemp,temp)
        else:
            temp-=1
    print(2**maxtemp)