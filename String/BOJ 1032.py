n=int(input())
data=list(input())
for _ in range(n-1):
    newdata=list(input())
    for j in range(len(data)):
        if newdata[j]!=data[j] and data[j]!="?":
            data[j]='?'

print(''.join(data))