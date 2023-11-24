while True:
    answer=0
    a=input()
    if a=="#":
        break
    l=1
    negflag=0
    j=1
    n=len(a)
    l=8**(n-1)
    for i in a:
        if i=="/":
            answer+=l*(-1)*j
        if i=="-":
            answer+=l*0*j
        elif i=="\\":
            answer+=l*1*j
        elif i=="(":
            answer+=l*2*j
        elif i=="@":
            answer+=l*3*j
        elif i=="?":
            answer+=l*4*j
        elif i==">":
            answer+=l*5*j
        elif i=="&":
            answer+=l*6*j
        elif i=="%":
            answer+=l*7*j
        j=1
        l//=8
    print(answer)
        
