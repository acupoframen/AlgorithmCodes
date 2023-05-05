while True:
    data=input()
    if data=="end":
        break
    xcount=0
    ocount=0
    data=list(data)
    if data[0]==data[4]==data[8]:
        if data[0]=='X':
            xcount+=1
        elif data[0]=='O':
            ocount+=1
    if data[2]==data[4]==data[6]:
        if data[2]=='X':
            xcount+=1
        elif data[2]=='O':
            ocount+=1
    if data[0]==data[1]==data[2]:
        if data[0]=='X':
            xcount+=1
        elif data[0]=='O':
            ocount+=1
    if data[3]==data[4]==data[5]:
        if data[3]=='X':
            xcount+=1
        elif data[3]=='O':
            ocount+=1
    if data[6]==data[7]==data[8]:
        if data[6]=='X':
            xcount+=1
        elif data[6]=='O':
            ocount+=1
    if data[0]==data[3]==data[6]:
        if data[0]=='X':
            xcount+=1
        elif data[0]=='O':
            ocount+=1
    if data[1]==data[4]==data[7]:
        if data[1]=='X':
            xcount+=1
        elif data[1]=='O':
            ocount+=1
    if data[2]==data[5]==data[8]:
        if data[2]=='X':
            xcount+=1
        elif data[2]=='O':
            ocount+=1
    if xcount>=1 and ocount>=1:
        print("invalid")
        continue
    if data.count("X")!=data.count("O") and data.count("X")!=data.count("O")+1:
        print("invalid")
        continue
    if ocount>=1:
        if data.count("X")==data.count("O")+1:
            print("invalid")
            continue
    if xcount>=1:
        if data.count("X")==data.count("O"):
            print("invalid")
            continue
    if xcount+ocount==0:
        if data.count(".")==0:
            print("valid")
        else:
            print("invalid")
        continue
    print("valid")    