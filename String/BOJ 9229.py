while True:
    n=input()
    if n=="#":
        break
    answer=0
    while True:
        temp=input()
        if temp=="#":
            if answer:
                print("Incorrect")
            else:
                print("Correct")
            break
            
        diffcount=0
        if len(n) == len(temp):
            for i in range(len(n)):
                if n[i]!=temp[i]:
                    diffcount+=1
            if diffcount!=1:
                answer=1
            n=temp
        else:
            n=temp
            answer=1
        