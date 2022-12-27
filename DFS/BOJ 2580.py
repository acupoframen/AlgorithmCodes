import sys
input=sys.stdin.readline
data,blank= [],[]
for i in range(9):
    data.append(list(map(int,input().split())))
    for j in range(9):
        if not data[i][j]:
            blank.append((i,j))

def check(x,y):
    existingNum=set()
    for i in range(9):
        existingNum.add(data[x][i])
        existingNum.add(data[i][y])
    xrange=[num for num in range((x//3)*3,(x//3)*3+3)]
    yrange=[num for num in range((y//3)*3,(y//3)*3+3)]
    for a in xrange:
        for b in yrange:
            existingNum.add(data[a][b])
    numbers=[num for num in range(1,10) if num not in list(existingNum)]
    return numbers

    
def dfs(idx):
    if len(blank)==idx:
        for i in range(9):
            print(*data[i])
        exit(0)
    x,y=blank[idx]
    numbers=check(x,y)
    for num in numbers:
        data[x][y]=num
        dfs(idx+1)
        data[x][y]=0

dfs(0)
