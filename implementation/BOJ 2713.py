t=int(input())
for _ in range(t):
    inputted=input()
    start=4
    if inputted[1]!=" ":
        start+=1
        r=inputted[0:2]
        if inputted[4]!=" ":
            start+=1
            c=inputted[3:5]
        else:
            c=inputted[3]
    else:
        r=inputted[0]
        if inputted[3]!=" ":
            c=inputted[2:4]
            start+=1
        else:
            c=inputted[2]

    msg=inputted[start:]

    r=int(r)
    c=int(c)
    data=list(list('0' for _ in range(c)) for _ in range(r))
    visited=list(list(0 for _ in range(c)) for _ in range(r))
    answerstring=""
    for i in msg:
        trans="00000"
        if i==" ":
            pass
        else:
            trans=str(bin(int(ord(i)-ord("A")+1)))[2:]
            while len(trans)!=5:
                trans="0"+trans
        answerstring+=trans
    currx=0
    curry=0
    dx=0
    dy=1
    for i in answerstring:
        visited[currx][curry]=1
        data[currx][curry]=i
        if dx==0 and dy==1:
            if curry+dy==c or visited[currx][curry+dy]:
                dx=1
                dy=0
                currx+=dx
                curry+=dy
                continue
        elif dx==1 and dy==0:
            if currx+dx==r or visited[currx+dx][curry]:
                dx=0
                dy=-1
                currx+=dx
                curry+=dy
                continue
        elif dx==0 and dy==-1:
            if curry+dy==-1 or visited[currx][curry+dy]:
                dx=-1
                dy=0
                currx+=dx
                curry+=dy
                continue
        elif dx==-1 and dy==0:
            if currx+dx==-1 or visited[currx+dx][curry]:
                dx=0
                dy=1
                currx+=dx
                curry+=dy
                continue
        currx+=dx
        curry+=dy
    for i in range(r):
        for j in range(c):
            print(data[i][j],end="")
    print()