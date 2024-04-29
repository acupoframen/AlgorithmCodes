data=list(map(int,input().split("/")))
if data[0]+data[2]<data[1] or data[1]==0:
    print("hasu")
else:
    print("gosu")