import sys
input=sys.stdin.readline

def pow(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    half=pow(a,b//2)
    if b%2:
        return half*half*a%1000000007
    else:
        return half*half%1000000007

n=int(input())
data=sorted(list(map(int,input().split())))
answer=0
for i in range(n):
    answer+=data[i]*(pow(2,i)-pow(2,n-i-1))

print(answer%1000000007)