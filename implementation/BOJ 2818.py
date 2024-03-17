dice=[4,5,1,2,6,3]
dx=[0,0,1]
dy=[1,-1,0] #right, left, down
d=0
answer=0
def roll(d):
    if d==0:
        dice[0],dice[2],dice[5],dice[4]=dice[4],dice[0],dice[2],dice[5]
    elif d==1:
        dice[0],dice[2],dice[5],dice[4]=dice[2],dice[5],dice[4],dice[0]
    else:
        dice[1],dice[2],dice[3],dice[4]=dice[4],dice[1],dice[2],dice[3]

r,c=map(int,input().split())

for i in range(r):
    answer+=dice[2]
    fullroll=(c-1)//4
    answer+=fullroll*(dice[0]+dice[2]+dice[4]+dice[5])
    more=(c-1)%4
    for i in range(more):
        roll(d)
        answer+=dice[2]
    if d==1:
        d=0
    else:
        d=1
    roll(2)

print(answer)