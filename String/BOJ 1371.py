import sys
data=[0 for _ in range(26)]
lines=sys.stdin.readlines()
for i in lines:
    for j in i:
        if ord('a')<=ord(j)<=ord('z'):
            data[ord(j)-ord('a')]+=1

answer=[]
for i in range(len(data)):
    if data[i]==max(data):
        answer.append(chr(ord('a')+i))

print(*sorted(answer), sep='')