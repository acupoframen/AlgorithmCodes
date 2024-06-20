n=int(input())
grundy=list(0 for _ in range(n+1))
grundy[2]=1
for i in range(3,n+1):
    s=set()
    for j in range(1,i):
        s.add(grundy[j-1]^grundy[i-j-1])
    s=sorted(s)
    temp=0
    for j in s:
        if j==temp:
            temp+=1
        else:
            break
    grundy[i]=temp
if grundy[n]:
    print(1)
else:
    print(2)