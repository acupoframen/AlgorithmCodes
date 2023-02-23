import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
data=[list([0 for _ in range(m+1)])]+list([0]+list(map(int,input().split())) for _ in range(n))
onesData=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        if data[i][j]==1:
            onesData.append([i,j])
answer=[]
if len(onesData)==2*k:
    print(0)
elif len(onesData)==k:
    print(len(onesData))
    for i in range(len(onesData)):
        print(onesData[i][0],onesData[i][1])
else:
    dx=[0,1,-1,0]
    dy=[1,0,0,-1]
    xs=[]
    ys=[]
    if len(onesData)==2*k-1:
        for i,j in onesData:
            xs.append(i)
            ys.append(j)
            ones=[]
            for kx in range(4):
                if 0<dx[kx]+i<=n and 0<dy[kx]+j<=m and data[dx[kx]+i][dy[kx]+j]==1:
                    ones.append(kx)
            if all(i in ones for i in [1,3])  or all ( i in ones for i in [0,1])  or all(i in ones for i in [0,2])  or all(i in ones for i in [2,3]):
                print(1)
                print(i,j)
                exit(0)
    answer=[]
    ys.sort()
    xs.sort()
    if len(set(xs))==1:
        n=len(ys)-k
        answer=ys[n:len(ys)-n]
        print(len(answer))
        for i in range(len(answer)):
            print(xs[0],answer[i] )

    else:
        n=len(xs)-k 
        answer=xs[n:len(xs)-n]    
        print(len(answer))
        for i in range(len(answer)):
            print(answer[i],ys[0])