from collections import deque
data=[]
for _ in range(4):
    data.append(deque(list(input())))

k=int(input())

rotatedata=[list(map(int,input().split())) for _ in range(k)]
def checkleft(num,direction):
    if num<0:
        return 
    if data[num][2]!=data[num+1][6]:
        checkleft(num-1,-direction)
        data[num].rotate(direction)

def checkright(num,direction):
    if num>3:
        return
    if data[num][6]!= data[num-1][2]:
        checkright(num+1,-direction)
        data[num].rotate(direction)

for i in range(k):
    num =rotatedata[i][0]-1
    direction=rotatedata[i][1]
    checkleft(num-1,-direction)
    checkright(num+1,-direction)
    data[num].rotate(direction)

answer=0
if data[0][0]=='1':
    answer+=1
if data[1][0]=='1':
    answer+=2
if data[2][0]=='1':
    answer+=4
if data[3][0]=='1':
    answer+=8
print(answer)