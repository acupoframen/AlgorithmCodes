n,m=map(int,input().split())
s=list(input())
acount=-1
answer=''
for i in range(n-1,-1,-1):
    if acount==-1:
        if s[i] not in ['A','E','I','O','U']:
            answer+=s[i]
            acount=0
    elif not acount or acount==1:
        if s[i]=='A':
            acount+=1
            answer+=s[i]
    elif acount==2:
        if len(answer)!=m:
            answer+=s[i]

if len(answer)==m:
    print("YES")
    print(answer[::-1])
else:
    print("NO")