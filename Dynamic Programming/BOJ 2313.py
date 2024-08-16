n=int(input())
answer=0
answers=[]
for i in range(n):
    num=int(input())
    data=list(map(int,input().split()))
    temp=-1e10
    maxtemp=-1e10
    maxleft=0
    maxright=0
    left=0
    right=0
    for j in range(num):
        if temp<0:
            temp=data[j]
            left=j
            right=j
        else:
            if temp>0:
                right+=1
            else:
                left=right=j
            temp+=data[j]
        if maxtemp<temp or (maxtemp==temp and right-left < maxright-maxleft):
            maxtemp= temp
            maxleft= left
            maxright= right
    answers.append([maxleft+1,maxright+1])
    answer+=maxtemp
print(answer)
for i in range(n):
    print(*answers[i])