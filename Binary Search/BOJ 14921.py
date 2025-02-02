n=int(input())
data=list(map(int,input().split()))
data.sort()
left=0
right=len(data)-1
answer=1e11
pos=1

def binary(l,r):
    global answer,pos
    target=data[l]
    l+=1
    while l<=r:
        mid=(l+r)//2
        if target+data[mid]>0:
            r=mid-1
        elif target+data[mid]<0:
            l=mid+1
        else:
            print(0)
            exit(0)
        answer=min(abs(answer),abs(target+data[mid]))
        if abs(answer)==abs(target+data[mid]):
            if target+data[mid]>0:
                pos=1
            else:
                pos=-1    
while left<right:
    binary(left,right)
    left+=1
print(pos*answer)