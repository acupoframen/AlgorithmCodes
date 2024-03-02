n=int(input())
data=list(map(int,input().split()))
data.sort()
answer=0
for i in range(n):
    num=data[i]
    left=0
    right=n-1
    while left!=right:
        temp=data[left]+data[right]
        if i==left:
            left+=1
            continue
        if i==right:
            right-=1
            continue
        if temp==num:
            answer+=1
            break
        elif temp<=num:
            left+=1
        elif temp>num:
            right-=1

print(answer)