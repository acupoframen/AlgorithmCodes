n=int(input())
data=input()
answer=0
temp=1
for i in range(n-1):
    if abs(ord(data[i])-ord(data[i+1]))==1:
        temp+=1
    else:
        temp=1
    answer=max(answer,temp)
if answer>=5:
    print("YES")
else:
    print("NO")