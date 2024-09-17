import math
n,m=map(int,input().split())
if  m:
    data=list(map(int,input().split()))
else:
    data=[]
answer=0
count=10
for i in range(m+1):
    answer+=((-1)**i)*pow(count,n)*math.comb(m,i)
    count-=1
print(answer)