s=input()
i=0
answer=""
while True:
    if i>=len(s):
        break
    if s[i:i+4]=='XXXX':
        i+=4
        answer+='AAAA'
    elif s[i:i+2]=='XX':
        i+=2
        answer+='BB'
    elif s[i]=='.':
        i+=1
        answer+='.'
    else:
        answer=-1
        break
print(answer)