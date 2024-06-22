
def manacher(s,n):
    a=[0 for _ in range(n)]
    r,p=0,0
    for i in range(n):
        if i<=r:
            a[i]=min(a[2*p-i],r-i)
        while i>=a[i]+1 and i+a[i]+1<n and s[i-a[i]-1]==s[i+a[i]+1]:
            a[i]+=1
        if r<i+a[i]:
            r=i+a[i]
            p=i
    return a
s="#"+"#".join(input())+"#"
n=len(s)
print(max(manacher(s,n)))