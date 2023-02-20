import sys
input=sys.stdin.readline
n,m=map(int,input().split())
inputted=list(map(int,input().split()))
nextdata=[0]*(10**6+1)
previousdata=[0]*(10**6+1)
for i in range(n-1):
    nextdata[inputted[i]]=inputted[i+1]
    previousdata[inputted[i+1]]=inputted[i]
nextdata[inputted[-1]]=inputted[0]
previousdata[inputted[0]]=inputted[-1]
for _ in range(m):
    func,*a=input().split()
    if func=="BN":
        i,j=map(int,a)
        print(nextdata[i])
        nextdata[i],nextdata[j]=j,nextdata[i]
        previousdata[nextdata[j]],previousdata[j]=j,i   
    elif func=="BP":
        i,j=map(int,a)
        print(previousdata[i])
        previousdata[i],previousdata[j]=j,previousdata[i]
        nextdata[previousdata[j]],nextdata[j]=j,i
    elif func=="CN":
        a=int(a[0])
        print(nextdata[a])
        nextdata[a]=nextdata[nextdata[a]]
        previousdata[nextdata[a]]=a
    else:
        a=int(a[0])
        print(previousdata[a])
        previousdata[a]=previousdata[previousdata[a]]
        nextdata[previousdata[a]]=a