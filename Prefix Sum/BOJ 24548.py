n=int(input())
data=list(input())
answer=0
dp= [[list(list(0 for _ in range(3)) for _ in range(3))  for _ in range(3)] for _ in range(3)]
dp[0][0][0][0]=1
tcount=0
gcount=0
fcount=0
pcount=0
for i in range(n):
    if data[i]=='T':
        tcount=(tcount+1)%3
    elif data[i]=='G':
        gcount=(gcount+1)%3
    elif data[i]=='F':
        fcount=(fcount+1)%3
    else:
        pcount=(pcount+1)%3
    answer+=dp[tcount][gcount][fcount][pcount]
    dp[tcount][gcount][fcount][pcount]+=1
print(answer)