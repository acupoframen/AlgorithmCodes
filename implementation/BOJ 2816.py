n=int(input())
data=[input() for _ in range(n)]
answer=''
a=0
b=0
for i in range(n):
    if data[i]=='KBS1':
        a=i
    elif data[i]=='KBS2':
        b=i

answer+='1'*a
answer+='4'*a
if a>b:
    b+=1
answer+='1'*b
answer+='4'*(b-1)
print(answer)