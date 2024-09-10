import sys
input=sys.stdin.readline
n=int(input())
answer=0
data=list(list(0 for i in  range(58)) for _ in range(58))

for _ in range(n):
    a,b=input().strip().split(" => ")
    if a!=b and not data[ord(a)-65][ord(b)-65]:
        data[ord(a)-65][ord(b)-65]=1
        answer+=1

for k in range(58):
    for i in range(58):
        for j in range(58):
            if i!=j and not data[i][j] and data[i][k] and data[k][j]:
                data[i][j]=1
                answer+=1

print(answer)
for i in range(58):
    for j in range(58):
        if data[i][j]:
            print(chr(i+65) + " => " + chr(j+65))