t = int(input())
data = [0] + [list(map(int, input())) for _ in range(t)]

def turn(temp, turnmode):
    if turnmode == 1:
        data[temp] = [data[temp][7]] + data[temp][:7]
    else:
        data[temp] = data[temp][1:] + [data[temp][0]]

def turnconst(num, mode, snapshot):
    currmode = mode
    currnum = num - 1
    while currnum >= 1:
        if snapshot[currnum + 1][6] == snapshot[currnum][2]:
            break
        turn(currnum, currmode)
        currmode *= -1
        currnum -= 1

    currmode = mode
    currnum = num + 1
    while currnum <= t:
        if snapshot[currnum - 1][2] == snapshot[currnum][6]:
            break
        turn(currnum, currmode)
        currmode *= -1
        currnum += 1

for _ in range(int(input())):
    num, d = map(int, input().split())
    snapshot =[0]+[row[:] for row in data[1:]] 
    turn(num, d)  
    turnconst(num, -d, snapshot)

answer = 0
for i in range(1, t + 1):
    if data[i][0] == 1:
        answer += 1
print(answer)
