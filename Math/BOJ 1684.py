import math
n=int(input())
data=list(map(int,input().split()))
data=list(set(data))  
answer=[]

for i in range(len(data)-1):
    for j in range(i+1,len(data)):
        temp=data[j]-data[i]
        answer.append(temp)
gcd=answer[0]
for i in range(1,len(answer)):
    gcd=math.gcd(gcd,answer[i])
print(gcd)