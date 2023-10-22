n=int(input())
answer=0
for i in range(1,n+1):
    data=list(map(int,str(i)))
    num=i+sum(data)
    if n==num:
        answer=i
        break

print(answer)