n,k,p,x=map(int,input().split())
data=[[0 for _ in range(10)] for _ in range(10)]

binarynums=[[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,0,1,1],
            [1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

x='0'*(k-len(str(x)))+str(x)
binaryx=[binarynums[int(i)] for i in x]
answer=0
for i in range(1,n+1):
    possible='0'*(k-len(str(i)))+str(i)
    binaryy=[binarynums[int(k)] for k in possible]
    changenum=0
    for j in range(0,k):
        if binaryx[j]!=binaryy[j]:
            for k1 in range(7):
                if binaryx[j][k1]!=binaryy[j][k1]:
                    changenum+=1
        if changenum>p:
            break
    if 0<changenum<=p:
        answer+=1

print(answer)