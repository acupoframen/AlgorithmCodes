s=input()
n=len(s)
zflag=0
zcount=0
acount=0
answer=0
aflag=0

s+='A'
for i in range(n+1):
    if i==n:
        if zflag==1:
            answer+=zcount*acount
        break
    if zflag and s[i]!='Z':
        zflag=0
        answer+=zcount*acount
        zcount=0
        acount=0
    if s[i]=='Z':
        zflag=1
        zcount+=1
    if s[i]=='A':
        acount+=1
    if zflag or ord(s[i+1])-ord(s[i])==0 or ord(s[i+1])-ord(s[i])==1:
        continue
    else:
        acount=0

print(answer)