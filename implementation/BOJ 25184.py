n=int(input())
answer=[]
if n==1:
    answer.append(1)
elif n%2==0:
    for i in range(n//2,-1,-1):
        answer.append(i)
        answer.append(i+n//2)
else:
    for i in range(n//2+1,-1,-1):
        answer.append(i)
        answer.append(i+n//2)
    answer.append(n//2+1)
for i in range(n):
    print(answer[i], end=' ')