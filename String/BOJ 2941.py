n=input()
n+='00'
count=0
i=0
while i<(len(n)):
    if n[i]=='0':
        break
    if n[i]=='c':
        if n[i+1]=='=' or n[i+1]== '-':
            i+=1
    elif n[i]=='d':
        if n[i+1:i+3]=='z=':
            i+=2
        elif n[i+1]=='-':
            i+=1
    elif n[i:i+2]=='lj' or n[i:i+2]=='nj' or n[i:i+2]=='s=' or n[i:i+2]=='z=':
        i+=1
    count+=1
    i+=1
print(count)