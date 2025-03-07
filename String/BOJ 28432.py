n=int(input())
data=list(input() for _ in range(n))
m=int(input())
possible=list(input() for _ in range(m))
question=data.index("?")
if n==1 or m==1:
    print(possible[0])
    exit(0)
if question==0:
    for i in range(m):
        if possible[i][-1]==data[question+1][0] and possible[i] not in data:
            print(possible[i])
            break

elif question!=n-1:
    for i in range(m):
        if possible[i][-1]==data[question+1][0] and possible[i][0]==data[question-1][-1] and possible[i] not in data:
            print(possible[i])
            break
        
else:
    for i in range(m):
        if possible[i][0]==data[question-1][-1] and possible[i] not in data:
            print(possible[i])
            break
        