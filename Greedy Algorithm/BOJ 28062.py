n=int(input())
even=[]
odd=[]
data=list(map(int,input().split()))
for i in data:
    if i%2:
        odd.append(i)
    else:
        even.append(i)

answer=sum(even)
if len(odd)%2:
    answer+=sum(sorted(odd)[1:])
else:
    answer+=sum(odd)
print(answer)