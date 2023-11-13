import sys
input=sys.stdin.readline

minus=[]
pos=[]
zero=[]
one=[]
n=int(input())
for i in range(n):
    num=int(input())
    if num<0:
        minus.append(num)
    elif num>1:
        pos.append(num)
    elif num==1:
        one.append(num)
    else:
        zero.append(num)

minus.sort(reverse=True)
pos.sort()

answer=[]
while len(minus)>=2:
    answer.append(minus.pop()*minus.pop())

while minus:
    if zero:
        zero.pop()
        minus.pop()
    else:
        answer.append(minus.pop())

while len(pos)>=2:
    answer.append(pos.pop() * pos.pop())
while pos:
    answer.append(pos.pop())
while one:
    answer.append(one.pop())

print(sum(answer))