import sys
def cal(a,b):
    return a**2 - b**2

g = int(input())
a,b = 1,1
answer=[]

while a+b <= g:
    if cal(a,b) == g :
        answer.append(a)
        a +=1
    elif cal(a,b) > g :
        b +=1
    elif cal(a,b) < g :
        a +=1
if not answer :
    print(-1)
for i in answer:
    print(i)