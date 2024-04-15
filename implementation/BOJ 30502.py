n,m=map(int,input().split())
data=[[-1,-1] for _ in range(n+1)]
for _ in range(m):
    a,b,c=input().split()
    a=int(a)
    c=int(c)
    if b=='P':
        if c==0:
            data[a][0]=0
        else:
            data[a][0]=1
    if b=='M':
        if c==0:
            data[a][1]=1
        else:
            data[a][1]=0

minanswer=0
maxanswer=0
for i in range(1,n+1):
    if data[i][0]==data[i][1]==1:
        minanswer+=1
    if data[i][0]!=0 and data[i][1]!=0:
        maxanswer+=1

print(minanswer,maxanswer)