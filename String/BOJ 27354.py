import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    st=list(input())
    if st[-1]=='\n':
        st=list(map(int,st[:-1]))
    else:
        st=list(map(int,st))
    if n==3 or n==1:
        print(-1)
        continue
    if n==2:
        if st[0]==st[1]:
            print(1)
        else:
            print(0)
        continue
    ones=[]
    zeros=[]
    for i in range(n):
        if st[i]==1:
            ones.append(i)
        else:
            zeros.append(i)
    if len(zeros)==0 or len(ones)==0:
        print(2)
        continue
    zerosdiff=zeros[-1]-zeros[0]
    onesdiff=ones[-1]-ones[0]
    if zerosdiff==onesdiff:
        print(0)
    elif zerosdiff==0 or onesdiff==0:
        tempcount=0
        if st[0]==1:
            tempcount+=1
        if st[1]==0:
            tempcount+=1
        if st[-2]==1:
            tempcount+=1
        if st[-1]==0:
            tempcount+=1
        if tempcount>2:
            tempcount=4-tempcount
        print(tempcount)
    else:
        if ones[0]-zeros[-1]==1 or zeros[0]-ones[-1]==1:
            if n%2 and abs(len(ones)-len(zeros))==1:
                print(2)
            else:
                print(1)
        elif zerosdiff==n-1 or onesdiff==n-1:
            tempcount=0
            if st[0]==1:
                tempcount+=1
            if st[1]==0:
                tempcount+=1
            if st[-2]==1:
                tempcount+=1
            if st[-1]==0:
                tempcount+=1
            if tempcount>2:
                tempcount=4-tempcount
            print(tempcount)
        else:
            print(1)

            #-> 92프로에서 틀림