import sys
input=sys.stdin.readline
while True:
    try:
        x=int(input())
        x*=int(1e7)
        n=int(input())
        data=list(int(input()) for _ in range(n))
        data.sort()
        start=0
        end=n-1
        flag=0
        while (start<end):
            if data[start]+data[end]==x:
                print("yes",data[start],data[end])
                flag=1
                break
            elif data[start]+data[end]<x:
                start+=1
            elif data[start]+data[end]>x:
                end-=1
        if not flag:
            print("danger")
    except:
        break