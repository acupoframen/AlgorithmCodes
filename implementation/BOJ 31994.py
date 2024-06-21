answer,answernumber=input().split()
for _ in range(6):
    a,b=input().split()
    if int(answernumber)<int(b):
        answer=a
        answernumber=b
print(answer)