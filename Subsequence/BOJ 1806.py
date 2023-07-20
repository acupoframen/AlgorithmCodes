n,s=map(int,input().split())
data=list(map(int,input().split()))
i,j=0,0
val=data[0]
answer=1e10
while True:
    if val >= s:
        val-=data[i]
        answer=min(answer, j-i+1)
        i+=1
    else:
        j+=1
        if j==n:
            break
        val+=data[j]
if answer==1e10:
    print(0)
else:
    print(answer)