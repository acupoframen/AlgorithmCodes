n,d=map(int,input().split())
data=list(map(int,input().split()))
curr=[-1e10,data[0]]
answer=[data[0]]
for i in data[1:]:
    temp=i
    flag=1
    for j in range(len(curr)-1):
        left,right=curr[j],curr[j+1]
        if right-d<i:
            continue
        elif left+d<=temp and temp<=right-d:
            curr.append(temp)
            answer.append(temp)
            curr.sort()
            flag=0
            break
        elif left+d<=right-d:
            temp=min(max(left+d,temp),right-d)
            curr.append(temp)
            answer.append(temp)
            curr.sort()
            flag=0
            break
        temp=right+d
    temp=max(i,right+d)
    if flag:
        curr.append(temp)
        answer.append(temp)
        curr.sort()

print(*answer)