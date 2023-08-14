n=int(input())
list1=list(map(int,input().split()))
m=int(input())
list2=list(map(int,input().split()))
list1.sort()
for i in list2:
    flag=0
    left, right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if i==list1[mid]:
            print (1)
            flag=1
            break
        
        elif i>list1[mid]:
            left=mid+1
        else:
            right=mid-1
    if not flag:
        print(0)