n=int(input())
data=[list(input()) for _ in range(n)]
def heartFinder():
    for i in range(n):
        for j in range(n):
            if data[i][j]=='*':
                return i+1,j

yPos,xPos=heartFinder()
print(yPos+1,xPos+1)
answer=0
for i in range(0,xPos):
    if data[yPos][i]=='*':
        answer+=1
print(answer, end=' ')
answer=0
for i in range(xPos+1,n):
    if data[yPos][i]=='*':
        answer+=1
print(answer, end=' ')
answer=0
for i in range(yPos+1,n):
    if data[i][xPos]=='*':
        answer+=1
    else:
        yPos=i
        break
print(answer, end=' ')
answer=0
for i in range(yPos,n):
    if data[i][xPos-1]=='*':
        answer+=1
    else:
        break
print(answer, end=' ')
answer=0
for i in range(yPos,n):
    if data[i][xPos+1]=='*':
        answer+=1
    else:
        break
print(answer)