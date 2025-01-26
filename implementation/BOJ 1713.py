n=int(input())
m=int(input())
data=list(map(int,input().split()))
count=[]
result=[]
for i in data:
    if i in result:
        count[result.index(i)]+=1
    else:
        if len(result)>=n:
            index=count.index(min(count))
            del result[index]
            del count[index]
        result.append(i)
        count.append(1)
result.sort()
print(*sorted(result))