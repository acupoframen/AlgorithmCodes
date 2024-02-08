import math
n=int(input())
data=list(map(int,input().split()))

def gcd(a,b):
    while a%b:
        a,b=b,a%b
    return b

def multiplegcd(start,end):
    temp=data[start]
    for i in range(start+1,end+1):
        temp=gcd(temp,data[i])
    return temp

def divide(start,end):
    if start==end:
        return data[start]
    mid1=start+math.floor((end-start+1)/2)-1
    mid2=end-math.ceil((end-start+1)/2)+1
    return max(divide(start,mid1)+multiplegcd(mid2,end),multiplegcd(start,mid1)+divide(mid2,end))

print(divide(0,n-1))