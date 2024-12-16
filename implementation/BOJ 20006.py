p,m=map(int,input().split())
room=[]
roomlevel=[]
for _ in range(p):
    l,n=input().split()
    l=int(l)
    flag=0
    for i in range(len(room)):
        if len(room[i])<m and abs(roomlevel[i]-l)<=10:
            room[i].append([l,n])
            flag=1
            break
    if not flag:
        roomlevel.append(l)
        room.append([[l,n]])
for i in range(len(room)):
    if len(room[i])<m:
        print("Waiting!")
    else:
        print("Started!")
    room[i].sort(key=lambda x:x[1])
    for j in range(len(room[i])):
        print(room[i][j][0],room[i][j][1])