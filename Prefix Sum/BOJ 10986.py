n,m=map(int,input().split())
data=list(map(int,input().split()))
remainders=list(0 for _ in range(m))
prefixsum=0
for i in range(n):
    prefixsum+=data[i]
    remainders[prefixsum%m]+=1
answer=remainders[0]
for i in range(m):
    answer+=remainders[i]*(remainders[i]-1)//2
print(answer)