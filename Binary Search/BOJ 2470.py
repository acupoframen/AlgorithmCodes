n=int(input())
data=list(map(int,input().split()))
data.sort()
left=0
right=len(data)-1
answer=1e11
answerleft=0
answerright=0

def binary(l,r):
    global answer,answerright,answerleft
    target=data[l]
    l+=1
    while l<=r:
        mid=(l+r)//2
        if target+data[mid]>0:
            r=mid-1
        elif target+data[mid]<0:
            l=mid+1
        else:
            print(target,data[mid])
            exit(0)
        if abs(answer)>abs(target+data[mid]):
            answerleft=target
            answerright=data[mid]
            answer=abs(target+data[mid])
        
while left<right:
    binary(left,right)
    left+=1
print(answerleft,answerright)