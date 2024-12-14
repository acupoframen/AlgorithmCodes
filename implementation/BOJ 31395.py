n=int(input())
data=list(map(int,input().split()))
answer=0
curr=1
for i in range(n-1):
    if data[i]<data[i+1]:
        curr+=1
    else:
        answer+=(curr*(curr+1))//2
        curr=1

print(answer+(curr*(curr+1))//2)