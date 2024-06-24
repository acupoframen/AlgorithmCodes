import math
s=input()
s="#"+"#".join(s)+"#"
n=len(s)

def manacher():
    a=list(0 for _ in range(n))
    r,p=0,0
    for i in range(n):
        if i<=r:
            a[i]=min(a[2*p-i],r-i)
        while i-a[i]-1>=0 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]:
            a[i]+=1
        if r<a[i]+i:
            r=a[i]+i
            p=i
    return a
temp=manacher()
answer=0
for i in temp:
    answer+=(i+1)//2
print(answer)