s=list(input())
zero=s.count('0')
one=s.count('1')
temp=0
skip=[0 for _ in range(len(s))]
for i in range(len(s)):
    if temp<one//2:
        if s[i]=='1':
            skip[i]=1
            temp+=1
temp=0
for i in range(len(s)-1,-1,-1):
    if temp<zero//2:
        if s[i]=='0':
            skip[i]=1
            temp+=1

for i in range(len(s)):
    if skip[i]==0:
        print(s[i],end='')