t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    b.sort()
    answer=0
    for i in a:
        left, right=0,m-1
        while left<right:
            mid=(left+right)//2
            if b[mid]<=i:
                left=mid+1
            else:
                right=mid
        if left==0:
            answer+= b[0]
        elif i-b[left-1]>b[left]-i:
            answer+=b[left]
        else:
            answer+=b[left-1]
    print(answer)
