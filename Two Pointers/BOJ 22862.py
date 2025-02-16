n,k=map(int,input().split())
data=list(map(int,input().split()))
end=0
answer=0
temp=0
odd=0
for start in range(n):
    while (odd<=k and end<n):
        if data[end]%2:
            odd+=1
        else:
            temp+=1
        end+=1
        if start==0 and end==n:
            answer=temp
            break
    if odd==k+1:
        answer=max(temp,answer)
    if data[start]%2:
        odd-=1
    else:
        temp-=1
print(answer)
