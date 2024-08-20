x=0
y=0
data=list(list(map(int,input().split())) for _ in range(9))
minval=0
for i in range(9):
    for j in range(9):
        if data[i][j]>minval:
            x=i
            y=j
            minval=data[i][j]

print(minval)
print(x+1,y+1)