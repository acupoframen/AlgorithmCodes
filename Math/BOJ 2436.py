def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a,b=map(int,input().split())
temp=b//a
answer1,answer2=0,0
for i in range(1,int(temp**0.5)+1):
    j=temp//i
    if i*j!=temp:
        continue
    if gcd(j,i)!=1:
        continue
    answer1,answer2=a*i,a*j
print(answer1,answer2)