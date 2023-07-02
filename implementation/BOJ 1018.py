n,m=map(int,input().split())
data=[list(input()) for _ in range(n)]
answer=64
for i in range(0,n-7):
    for j in range(0,m-7):
        count=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if data[k][l]=='B':
                        count+=1
                elif (k+l)%2==1:
                    if data[k][l]=='W':
                        count+=1
        count=min(count,64-count)
        answer=min(answer,count)
print(answer)