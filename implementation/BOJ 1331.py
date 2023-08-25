curr=list(input())
data=[[0 for _ in range(6)] for _ in range(6)]
start=curr
data[ord(curr[0])-ord('A')][int(curr[1])-1]=2
for i in range(35):
    now=list(input())
    if data[ord(now[0])-ord('A')][int(now[1])-1]==0 and i!=34:
        if abs(ord(curr[0])-ord(now[0]))==2 and abs(int(curr[1])- int(now[1]))==1:
            data[ord(now[0])-ord('A')][int(now[1])-1]=1
            curr=now
        elif abs(ord(curr[0])-ord(now[0]))==1 and abs(int(curr[1])-int(now[1]))==2:
            data[ord(now[0])-ord('A')][int(now[1])-1]=1
            curr=now
        else:
            print('Invalid')
            exit(0)
    else:
        if i==34  and data[ord(now[0])-ord('A')][int(now[1])-1]==0 and ((abs(ord(start[0])-ord(now[0]))==2 and abs(int(start[1])- int(now[1]))==1 )or (abs(ord(start[0])-ord(now[0]))==1 and abs(int(start[1])-int(now[1]))==2)):
            continue
        else:
            print('Invalid')
            exit(0)

print('Valid')