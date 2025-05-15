from math import gcd,lcm
a=list(map(int,input().split()))
b=list(map(int,input().split()))
answer=[a[0]*b[1]+a[1]*b[0],a[1]*b[1]]
g=gcd(answer[0],answer[1])
answer[0]//=g
answer[1]//=g  
print(answer[0],answer[1])
