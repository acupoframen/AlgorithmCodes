n=int(input())
for _ in range(n):
    data=[[0 for _ in range(10)] for _ in range(3)]
    inputs=list(input().split())
    for j in range(4):
        a,b=inputs[j][0],inputs[j][1]
        a=int(a)
        if b=='m':
            data[0][0]+=1
            data[0][a]+=1
        elif b=='p':
            data[1][0]+=1
            data[1][a]+=1
        else:
            data[2][0]+=1
            data[2][a]+=1
    satis=False
    two=0
    for i in range(3):
        if satis:
            break
        for j in range(1,10):
            if data[i][j]>=3:
                satis=True
                break
            if data[i][j]==2:
                two+=1
                if two==2:
                    satis=True
                    break
            if 2<=j<=8 and data[i][j-1]>0 and data[i][j]>0 and data[i][j+1]>0:
                satis=True
                break
    if satis:
        print(":)")
    else:
        print(":(")