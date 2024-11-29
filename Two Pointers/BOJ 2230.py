n,m=map(int,input().split())
data=list(int(input()) for _ in range(n))
data.sort()
left=0
right=0
answer=1e10
while right<n and left<n:
    if data[right]-data[left]>=m:
        answer=min(data[right]-data[left],answer)
        left+=1
    else:
        right+=1
print(answer)