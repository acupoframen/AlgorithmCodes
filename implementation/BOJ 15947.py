n=int(input())
rucount=1+n//14
if n%14==1 or n%14==13:
    print("baby")
elif n%14==2 or n%14==0:
    print("sukhwan")
elif n%14==5:
    print("very")
elif n%14==6:
    print("cute")
elif n%14==9:
    print("in")
elif n%14==10:
    print("bed")
elif n%14 in (3,7,11):
    if rucount>=4:
        print("tu+ru*",rucount+1,sep="")
    else:
        print("tu","ru"*(rucount+1),sep="")
else:
    if rucount>=5:
        print("tu+ru*",rucount,sep="")
    else:
        print("tu","ru"*(rucount),sep="")
    
