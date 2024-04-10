n,m=map(int,input().split())
s=list(input())
acount=-1
answer=[]
for i in range(n-1,-1,-1):
    if acount==-1:
        if s[i] not in ['A','E','I','O','U']:
            answer.append(s[i])
            acount=0
    elif acount==0 or acount==1:
        if s[i]=='A':
            acount+=1
            answer.append(s[i])
    elif acount==2:
        if len(answer)!=m:
            answer.append(s[i])

if acount==2  and len(answer)==m:
    print("YES")
    print(''.join(answer[::-1]))
else:
    print("NO")