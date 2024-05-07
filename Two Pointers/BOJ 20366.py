n=int(input())
data=list(map(int,input().split()))
data.sort()
answer=1e10
for i in range(n-1):
    for j in range(i+1,n):
        a=i+1
        b=j-1
        if b<=a:
            continue
        while a<b:
            val=data[i]+data[j]-data[a]-data[b]
            answer=min(answer,abs(val))
            if val==0:
                print(0)
                exit(0)
            elif val>0:
                a+=1
            else:
                b-=1
print(answer)