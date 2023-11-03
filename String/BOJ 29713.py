n=int(input())
s=input()
data=[0 for _ in range(10)]
for i in range(n):
    if s[i]=='B':
        data[0]+=1
    elif s[i]=='R':
        data[1]+=1
    elif s[i]=='O':
        data[2]+=1
    elif s[i]=='N':
        data[3]+=1
    elif s[i]=='Z':
        data[4]+=1
    elif s[i]=='E':
        data[5]+=1
    elif s[i]=='S':
        data[6]+=1
    elif s[i]=='I':
        data[7]+=1
    elif s[i]=='L':
        data[8]+=1
    elif s[i]=='V':
        data[9]+=1
data[5]//=2
data[1]//=2
print(min(data))